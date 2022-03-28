# spotify-chart

1. chromedriver.exe 설치

   1. 크롬 버전 확인
      1. https://support.google.com/chrome/answer/95414?hl=ko&co=GENIE.Platform%3DDesktop
   2. chromedriver.exe 설치
      1. https://chromedriver.chromium.org/downloads
      2. chromedriver_win32.zip  등 os에 맞게 설치후 소스코드 위치에 압축풀면 됨

2. python 라이브러리 설치

   1. `python -m pip install -r requirements.txt`
   2. 설치하기 어려우면 winpython으로 진행 (윈도우의 경우)
   3. https://github.com/winpython/winpython/releases/download/4.6.20220116/Winpython64-3.8.12.1PyPy.exe

3. 스크립트 실행

   1. 10~12번째줄 START, END, REGION 변경해서 커스터마이징 가능

      1. START: 시작 날짜. YYYY-MM-DD 형태로 적어야함
      2. END: 끝 날짜. YYYY-MM-DD 형태로 적어야함
      3. REGION: 지역. 기본: global, 한국: kr, 지역코드는 확인바람

      ```python
      START = "2022-03-01"
      END = "2022-03-27"
      REGION = "global"
      ```

4. csv 파일은 소스코드 위치에 저장됨

   1. 파일명은 `spotifychart-{region}-{start}-to-{end}.csv` 형태
   2. encoding은 기본 utf-8, 엑셀로 열때 인코딩 설정안하면 글짜 깨질 수 있음.

