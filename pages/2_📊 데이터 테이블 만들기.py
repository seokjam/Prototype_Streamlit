import streamlit as st
import pandas as pd

st.header('📊 데이터 테이블 만들기')

st.subheader("1. 데이터 불러오기")
st.markdown("데이터를 불러와서 데이터프레임에 저장합니다.")
st.markdown("> 데이터를 불러올 때는 :green['pandas'] 라이브러리를 사용합니다. \n \n  "
            "> 실습은 kaggle이 제공하는 **'S&P 500 Stocks (daily updated)'** 데이터 셋(CC0)에서,\n\n"
            "> ***'상위 10개 기업'***, ***'2022년'*** 주가만 추출한 데이터를 사용합니다.\n")

st.code("import pandas as pd\n\n"
        "stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'\n"
        "index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'\n"
        "df_stocks = pd.read_csv(stocks_file)\n"
        "df_index = pd.read_csv(index_file)")

df_stocks = pd.read_csv("./data/sp500_stocks_2022.csv")
df_index = pd.read_csv("./data/sp500_index_2022.csv")
st.markdown("---")
st.subheader("2. 데이터 프레임 출력하기")
st.markdown("불러온 데이터를 데이터 프레임 형태로 출력이 가능합니다.")

st.markdown("- #### 기본 데이터 프레임 출력하기")
st.code("st.dataframe(df_stocks)")
st.dataframe(df_stocks)

st.markdown("- #### Pandas 스타일링 적용하기(ex.Highlight)")
st.code("st.dataframe(df_index.style.highlight_max(axis=0))")
st.dataframe(df_index.style.highlight_max(axis=0))
st.markdown("---")

st.subheader("3. 조건을 선택하여 데이터 출력하기")
st.markdown("SelectBox, MultiSelectBox 등 다양한 Input 위젯을 사용하면 원하는 조건의 데이터만 출력할 수 있습니다.")

st.markdown("- #### Select Box 사용하기")
st.markdown("> st.selectbox(label, options)\n"
            "> - label은 Select Box를 설명하는 문구\n"
            "> - options은 Select 수 있는 목록")
st.code("symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))\n"
        "st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])\n")
symbol = st.selectbox('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()))
st.dataframe(df_stocks[df_stocks['Symbol'] == symbol])

st.markdown("- #### Multi Select Box 사용하기")
st.markdown("> st.multiselect(label, options)\n"
            "> - label : Multi Select Box를 설명하는 문구\n"
            "> - options : Select 할 수 있는 목록"
            "> - default : 기본으로 Select 되어 있는 값")
st.code("symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL', key='df')\n"
        "st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])")

symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL', key='df')
st.dataframe(df_stocks[df_stocks['Symbol'].isin(symbol_list)])

