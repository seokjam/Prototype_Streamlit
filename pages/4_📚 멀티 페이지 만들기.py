import streamlit as st

st.header("📚 멀티 페이지 만들기")

st.subheader("1. 디렉토리 만들기")
st.markdown("#### ① Pycharm 프로젝트 창에서 마우스 우클릭 'New > Directory' 선택\n")
st.image("./image/3-1.Create Directory.jpg")

st.markdown("#### ② 'New Directory' 창이 뜨면 ***:green['pages']*** 이름으로 새 디렉토리를 만듭니다. \n")
st.image("./image/3-2.New Directory Name.jpg")
st.markdown("---")

st.subheader("2. 파일 이름을 규칙에 맞춰 파이썬 파일(.py) 만들기")
st.markdown("#### ① Pycharm 프로젝트 ***:green['Pages'] 디렉토리 위에서 마우스 우클릭 'New > Python File' 선택\n")
st.image("./image/3-3.Create File.jpg")

st.markdown("#### ②  'New Python File' 창이 뜨면 다음과 같은 규칙의 이름으로 Python 파일을 만듭니다.\n")
st.markdown("- 파일 이름 규칙 : :red['숫자'] + '_' + :blue['메뉴 이름']")
st.image("./image/3-4.New Python File.jpg")

st.markdown("- 동일한 파일 이름 규칙으로 숫자를 증가시켜 페이지를 추가할 수 있습니다.")
st.image("./image/3-5.Pages Add.jpg")