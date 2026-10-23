# 생명의 빛 감리교회 홈페이지

정적 홈페이지 + GitHub Actions 기반 콘텐츠 관리자입니다.

## 구조
- `index.html`: 공개 교회 홈페이지 (반응형)
- `assets/`: CSS와 페이지 렌더링/포스터 슬라이드
- `data/content.json`: 설교·주보·앨범·행사·카테고리·교회 정보
- `admin/`: 브라우저 관리자 (GitHub API 사용)
- `scripts/update_content.py`: 관리자 입력 검증, JSON 갱신
- `.github/workflows/update-content.yml`: 업데이트 처리 및 커밋
- `.github/workflows/deploy.yml`: Pages 배포

## 최초 설정
1. GitHub 저장소 Settings → Pages → Build and deployment → Source에서 **GitHub Actions** 선택.
2. 저장소 Settings → Actions → General → Workflow permissions에서 콘텐츠 쓰기 권한 설정이 필요한 경우 **Read and write permissions**를 선택.
3. Actions 탭에서 **Deploy church website** 워크플로 실행.
4. Pages 주소가 발급되면 `/admin/`에 접속해 GitHub Fine-grained PAT로 인증.
5. PAT 권한: 해당 저장소 **Contents: Read and write**, **Actions: Read and write**. 가능한 짧은 만료일과 최소한의 권한으로 발급하세요.
6. 관리자에서 새 글 등록 → Update church content 실행 → `data/content.json` 커밋 → Deploy 실행.

## 관리자 운영
- 관리 화면에서 게시물을 등록·수정·삭제할 수 있습니다.
- 이미지 업로드는 GitHub Contents API를 이용하고, JSON 수정은 Actions를 통해 커밋합니다.
- 이미지는 4MB 이하 JPEG/PNG/WebP/GIF 지원.
- 저장 요청 후 GitHub Actions가 완료되면 다시 "콘텐츠 불러오기"를 눌러 확인합니다.
- 토큰은 브라우저 메모리에만 사용하지만, 관리자 페이지에서 발급받은 토큰을 입력하므로 공용 컴퓨터에서 사용하지 마세요.
- 관리자 HTML은 공개되므로 **관리자 주소 자체는 인증 수단이 아닙니다**. 권한은 GitHub PAT로 통제합니다.

## 주의사항
- 현재 리포지토리는 **Private** 상태입니다. GitHub 요금제 및 Pages 정책에 따라 비공개 저장소의 Pages 공개 배포가 불가능할 수 있습니다. 공개 홈페이지 운영 전 Pages 설정을 확인하세요.
- `data/content.json`은 홈페이지에서 로드하므로 개인정보나 보안 정보를 넣지 마세요.
- 파일 업로드는 JSON 갱신과 별개의 커밋입니다. 워크플로 실패 시 이미지 파일만 남을 수 있습니다.
- 게시글 본문은 텍스트로 출력합니다.
- GitHub Actions/Pages 실제 성공 여부는 Actions 화면에서 확인하세요.
