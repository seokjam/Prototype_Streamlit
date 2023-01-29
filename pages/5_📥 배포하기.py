import streamlit as st

st.header("📥 배포하기")

st.subheader("1. Github Repository 생성하기")
st.markdown("#### ① Pycharm 메뉴에서 'VCS > Create Git Repository' 선택 \n")
st.image("./image/5-1.Create Git Repository.jpg")

st.markdown("#### ② Git Repository를 생성하고자 하는 프로젝트 디렉토리 선택 \n")
st.image("./image/5-2.Select directory.jpg")

st.markdown("- 디렉토리 선택 후 우측 상단에 Git Menu 생성 확인 [**:blue[↙(Pull)]**, :green[✔(Commit)], **:green[↗(Push)]]**")
st.image("./image/5-4.Git Menu Button.jpg")

st.markdown("#### ③ Git :green[✔(Commit)] 하기\n")
st.markdown("- Unversioned Files 체크 박스를 체크하여 프로젝트의 파일들을 추가 후 하단의 'Commit' 클릭")
st.image("./image/5-3.Git Commit.jpg")

st.markdown("#### ④ Pycharm 메뉴에서 'Git > GitHub > Share Project GitHub' 선택하여 Repository 생성과 :green[↗(Push)] 완료하기\n")
st.image("./image/5-4.Share Project On GitHub.jpg")
st.markdown("- GitHub 사이트에 접속하여 Repository 생성이 완료된 것을 확인")
st.image("./image/5-5.GitHub Push.jpg")
st.markdown("---")

st.subheader("2. Streamlit 회원 가입하기")
st.markdown("#### ① [Streamlit(https://streamlit.io/)](https://streamlit.io/) 사이트 접속하기\n")
st.markdown("우측 상단 ***:red['Sign up']*** 버튼 클릭")
st.image("./image/0-4.Streamlit Site.jpg")
st.markdown("#### ② 'Continue with Google' 또는 'Continue with GitHub'을 선택하여 회원 가입 완료하기\n")
st.image("./image/0-5.Streamlit Sign up.jpg")
st.caption(" **Streamlit Cloud 배포를 위해선 :green[GitHub] 아이디가 필요합니다. 가급적 :green[GitHub] 아이디로 회원 가입을 추천 드립니다.**")
st.markdown("---")

st.subheader("3. Streamlit Cloud에 New App 추가하기")
st.markdown("#### ① 계정을 로그인 후 화면에서 'New app' 버튼 클릭합니다.\n")
st.image("./image/5-6.New App.jpg")
st.markdown("#### ② Deploy an app 화면에서 GitHub Repository 관련 정보를 입력하고 Deploy 버튼을 클릭합니다.\n"
            "> - Repository : Github Repository URL(https://github.com/ 다음 주소)\n"
            "> - Branch : master (또는 Main Branch 설정 값)\n"
            "> - Main file path : Main.py")
st.image("./image/5-7.Deploy an app.jpg")
st.markdown("- 'Your app is in the oven' 이라는 메시지가 뜬 후 몇 분이 지난 후,\n"
            " 'localhos:8501'에 뜨던 웹 페이지가 확인된다면 배포가 완료된 것입니다.")

st.markdown("---")
st.subheader("[Tip] 별도의 패키지(또는 특정 버전)를 설치한 경우")
st.markdown("Python으로 프로젝트를 진행하게 되면 pip로 여러 패키지를 설치하는 경우가 발생합니다.\n"
            "그런 경우 배포되는 서버에도 동일한 패키지들이 설치되어 있어야 합니다.\n"
            "이 때, pip로 설치된 패키지 리스트를 'requirements.txt'로 저장해 두면 Streamlit Coloud에서 자동으로 설치가 진행됩니다.\n")
st.markdown("- 터미널 창에서 다음 명령어를 실행하면 설치된 패키지 리스트를 확인할 수 있습니다.")
st.code("pip list")
st.markdown("- 터미널 창에서 다음 명령어를 실행하여 패키지 목록을 저장한 'requirements.txt' 파일을 생성합니다.")
st.code("pip list --format=freeze > requirements.txt")
st.markdown("- 생성된 'requirements.txt' :green[✔(Commit)], **:green[↗(Push)]]** 하여 완료합니다.\n")

st.markdown("---")
st.markdown("## 축하 드립니다.🎊🎊🎊🎊🎊\n")
st.markdown("#### 이제 어디서든 누구나 접속 가능한 여러분의 웹 페이지를 만드셨습니다.\n")