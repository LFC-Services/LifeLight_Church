import json, os, pathlib, re

PATH = pathlib.Path('data/content.json')
TYPES = {'sermons', 'bulletins', 'albums', 'events'}

def main():
    payload = json.loads(os.environ['CONTENT_PAYLOAD'])
    db = json.loads(PATH.read_text(encoding='utf-8'))
    op, typ = payload.get('op'), payload.get('type')
    if typ not in TYPES:
        raise ValueError('Invalid content type')
    if op == 'upsert':
        rec = payload['record']
        for key in ('id', 'title', 'category', 'date', 'body', 'image', 'link'):
            if not isinstance(rec.get(key, ''), str):
                raise ValueError('Invalid field: '+key)
        if not rec.get('id') or not rec.get('title') or len(json.dumps(rec, ensure_ascii=False)) > 18000:
            raise ValueError('Invalid record')
        items = [item for item in db[typ] if item['id'] != rec['id']]
        items.insert(0, {k: rec.get(k, '') for k in ('id', 'title', 'category', 'date', 'body', 'image', 'link')})
        db[typ] = items
    elif op == 'delete':
        db[typ] = [item for item in db[typ] if item['id'] != payload['id']]
    elif op == 'categories':
        if typ == 'events':
            raise ValueError('Invalid category type')
        values = payload['values']
        if not isinstance(values, list) or len(values) > 50 or any(not isinstance(s, str) or len(s)>50 for s in values):
            raise ValueError('Invalid categories')
        db['categories'][typ] = list(dict.fromkeys(values))
    else:
        raise ValueError('Invalid operation')
    PATH.write_text(json.dumps(db, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

if __name__ == '__main__':
    main()
