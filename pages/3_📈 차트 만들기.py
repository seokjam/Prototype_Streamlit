import streamlit as st
import pandas as pd

st.header("📈 차트 그리기")

st.subheader("1. 데이터 불러오기")
st.markdown("데이터를 불러와서 데이터프레임에 저장합니다.")
st.markdown("> 데이터를 불러올 때는 :green['pandas'] 라이브러리를 사용합니다. \n \n  "
            "> 실습은 kaggle이 제공하는 **'S&P 500 Stocks (daily updated)'** 데이터 셋(CC0)에서,\n\n"
            "> ***'상위 10개 기업'***, ***'2022년'*** 주가만 추출한 데이터를 사용합니다.\n")

st.code("import pandas as pd\n\n"
        "stocks_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_stocks_2022.csv'\n"
        "index_file = 'https://raw.githubusercontent.com/seokjam/stremlitProject/master/data/sp500_index_2022.csv'\n"
        "df_stocks = pd.read_csv(stocks_file)"
        "df_index = pd.read_csv(index_file")

df_stocks = pd.read_csv("./data/sp500_stocks_2022.csv")
df_index = pd.read_csv("./data/sp500_index_2022.csv")
st.markdown("---")

st.subheader("2. Line Chart 출력하기")
st.markdown("불러온 데이터를 Line Chart로 출력합니다.")
st.markdown("- #### 단일 데이터 출력하기")
st.code("st.line_chart(df_index, x='Date')")
st.line_chart(df_index, x='Date')

st.markdown("- #### 여러 데이터 출력하기")
st.markdown("> 복수의 데이터를 차트로 그리기 위해서는 데이터 수정이 필요합니다.")
df_chart = pd.DataFrame(columns=['Date'])
df_chart['Date'] = df_stocks['Date'].unique()
for symbol in df_stocks['Symbol'].unique():
	df_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)
st.dataframe(df_chart.head())

st.code("df_chart = pd.DataFrame(columns=['Date'])\n"
        "df_chart['Date'] = df_stocks['Date'].unique()\n"
        "\n"
        "for symbol in df_stocks['Symbol'].unique():\n"
        "\tdf_chart[symbol] = df_stocks[df_stocks['Symbol'] == symbol]['Close'].reset_index(drop=True)\n"
        "\n"
        "st.line_chart(df_chart, x='Date')")

st.line_chart(df_chart, x='Date')

st.subheader("3. Bar Chart 출력하기")
st.markdown("불러온 데이터를 bar Chart로 출력합니다.")
st.bar_chart(df_index.tail(21), x='Date')

st.subheader("4. 조건을 선택하여 차트 출력하기")
st.markdown("SelectBox, MultiSelectBox 등 다양한 Input 위젯을 사용하면 원하는 조건의 데이터만 출력할 수 있습니다.")

st.markdown("- #### Multi Select Box 사용하기")
st.markdown("> st.multiselect(label, options)\n"
            "> - label : Multi Select Box를 설명하는 문구\n"
            "> - options : Select 할 수 있는 목록\n"
            "> - default : 기본으로 Select 되어 있는 값")
st.code("symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')\n"
        "symbol_list.insert(0, 'Date')\n\n"
        "st.line_chart(df_chart[symbol_list], x='Date')")
symbol_list = st.multiselect('검색하고자 하는 기업을 선택하세요.', (df_stocks['Symbol'].unique()), default='AAPL')
symbol_list.insert(0, 'Date')
st.line_chart(df_chart[symbol_list], x='Date')
