import streamlit as st
import pandas as pd

st.header("📈 차트 그리기")

# 테이터 불러오기
df = pd.read_csv('./data/sp500_index.csv')


