import streamlit as st

st.title("📝 텍스트 입력하기")
st.markdown("Streamlit은 다양한 형태로 텍스를 입력할 수 있습니다.")

st.subheader("1. Title 입력하기")
st.markdown("제목 형식의 텍스트를 표시합니다.")
st.code("st.title('📌Title을 입력하세요.')\n")
st.title("📌Title을 입력하세요.")
st.markdown("---")

st.subheader("2. Header, Subheader 입력하기")
st.markdown("헤더(머리글)과 세부 헤더 항목으로 텍스트를 표시합니다.")
st.code("st.header('Header(머리글)을 입력하세요.')\n"
        "st.subheader('Subheader(세부 머리글)을 입력하세요.')")
st.header("Header(머리글)을 입력하세요.")
st.subheader("Subheader(세부 머리글)을 입력하세요.")
st.markdown("---")

st.subheader("3. Markdown 입력하기")
st.markdown("마크다운 포맷으로 입력이 가능합니다.")
st.markdown("- 헤더(Headers) 가장 ***큰 제목(H1)*** 부터 가장 ***작은 제목(H6)*** 까디 6단계로 사용 가능합니다.  ")
st.code("st.markdown('# H1 #')\n"
        "st.markdown('## H2 ##')\n"
        "st.markdown('### H3 ###')\n"
        "st.markdown('#### H4 ####')\n"
        "st.markdown('##### H5 #####')\n"
        "st.markdown('###### H6 ######')\n")
st.markdown('# H1 #')
st.markdown('## H2 ##')
st.markdown('### H3 ###')
st.markdown('#### H4 ####')
st.markdown('##### H5 #####')
st.markdown('###### H6 ######')
st.markdown("- 목록으로 글을 작성할 수 있습니다.\n")
st.code("# 순서가 있는 목록(숫자+점'.' 사용)\n"
        "st.markdown('1. 하나)\n"
        "st.markdown('2. 둘)\n"
        "st.markdown('3. 셋)\n"
        "# 순서가 없는 목록(글 머리 기호 '*, +, -' 사용\n"
        "st.markdown('* 하나')\n"
        "st.markdown('* 둘')\n"
        "st.markdown('* 셋')\n")
st.markdown('1. 하나')
st.markdown('2. 둘')
st.markdown('3. 셋')
st.markdown('* 하나')
st.markdown('* 둘')
st.markdown('* 셋')
st.markdown("---")

st.subheader("4. Caption 입력하기")
st.markdown("Caption은 캡션, 여백, 각주 및 기타 설명 텍스트로 출력 시 사용합니다.")
st.code("st.caption('이것은 Caption 입니다.')\n")
st.markdown("---")

st.subheader("5. 그 외 Text 형식 입력하기")
st.code("st.text('기본 텍스트를 입력합니다.')\n"
        "st.code('코드 블록 표시가 가능합니다.')")
st.text('기본 텍스트를 입력합니다.')
st.code('코드 블록 표시가 가능합니다.')
