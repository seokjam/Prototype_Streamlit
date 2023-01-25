import pandas as pd
import streamlit as st
import datetime

# Config pages
st.set_page_config(
    page_title="한국투자증권 신입사원 DT 프로젝트",
    page_icon="💰",
    layout="wide"
)

# Text elements
st.title("💰한국투자증권 신입사원 **:red[DT]** 프로젝트")
st.header("Streamlit 프로토타입 만들기")
st.subheader("1. [Streamlit](https://streamlit.io/)이란?")
st.markdown("***'A faster way to build and share data apps'***\n\n"
            "Streamlit 은 데이터 프로토타이핑 (Data Prototyping) 도구입니다.\n\n"
            "간단한 기능을 가진 데이터 웹 어플리케이션을,\n\n"
            "빠르고 간단하게 눈으로 확인할 수 있는 웹 형태로 만들 수 있다는 것이 가장 큰 장점입니다.")
st.markdown("**[장점]**\n"
            "> - Python 환경이기에 초보자도 쉽게 사용할 수 있습니다.\n"
            "> - Streamlit 패키지 설치 후 적절한 함수만 호출하면 사용할 수 있습니다.\n"
            "> - Script를 업데이트 할 때 마다 변경사항을 바로 확인 가능합니다.")
st.markdown("---")

st.subheader("2. Streamlit 회원 가입하기")
st.markdown("#### ① [Streamlit(https://streamlit.io/)](https://streamlit.io/) 사이트 접속하기\n")
st.markdown("우측 상단 ***:red['Sign up']*** 버튼 클릭")
st.image("./image/0-4.Streamlit Site.jpg")
st.markdown("#### ② 'Continue with Google' 또는 'Continue with GitHub'을 선택하여 회원 가입 완료하기\n")
st.image("./image/0-5.Streamlit Sign up.jpg")
st.caption(" **Streamlit Cloud 배포를 위해선 :green[GitHub] 아이디가 필요합니다. 가급적 :green[GitHub] 아이디로 회원 가입을 추천 드립니다.**")
st.markdown("---")

st.subheader("2. Streamlit 시작하기")
st.markdown("#### ① PyCharm(파이참) 실행 및 프로젝트 생성하기\n")
st.image("./image/0-1.Create Project.jpg")
st.caption("Pycharm을 실행하고 'New Project' 버튼을 클릭합니다.")
st.image("./image/0-2.Conda Env Project Create.jpg")
st.caption(" **'Location'** 에 신규 프로젝트 생성 디렉토리를 입력하고,\n"
           "'Python Interpreter를 New environment using을 Conda로 설정한 뒤 **'Create'** 를 클릭합니다.")
st.markdown("---")

st.markdown("#### ② Streamlit 설치하기 \n\n"
            "Terminal(터미널) 창을 열고 다음 명령어를 실행합니다.")
st.code("pip install streamlit")
st.markdown("---")

st.markdown("#### ③ Streamlit 실행하기 \n\n"
            " **'Main.py'** 라는 파이썬 파일을 하나 만들고, 아래의 코드를 복사하여 붙여넣고 저장합니다.")
st.code("import streamlit as st\n\n"
        "st.set_page_config(\n"
        "\tpage_title='Streamlit 프로토타입 만들기',\n"
        "\tpage_icon='🎈',\n"
        "\tlayout='wide'\n"
        ")\n"
        "\n"
        "st.text('🎈Streamlit 프로토타입 만들기')")
st.markdown(" 터미널 창에서 다음 명령어를 실행합니다.")
st.code("streamlit run Main.py")
st.markdown("---")

st.markdown(" **'http://localhost:8501/'** 주소로 다음과 같은 페이지가 출력되는지 확인합니다.")
st.image("./image/0-3.Run Streamlit.jpg")
st.markdown('---')
st.markdown("## 축하 드립니다.🎉🎉🎉\n")
st.markdown("#### 이제 여러분은 나만의 웹 페이지를 만드셨습니다.\n"
            "#### Streamlit의 기본 기능들은 왼쪽 메뉴에서 살펴 볼 수 있습니다.")

