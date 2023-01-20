import streamlit as st
import pandas as pd

st.header('📊 데이터 테이블 만들기')

# 테이터 불러오기
df = pd.read_csv('./data/sp500_index.csv')

st.dataframe(df)

