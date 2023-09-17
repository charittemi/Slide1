﻿# streamlit >streamlit run main.py

import streamlit as st

st.title('Slide(確認中)')
st.caption('mdファイルから作成したhtmlを埋め込んでいます')
st.text('')

# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=800, height=600)
st.text('')
st.subheader('コード')
code='''
# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=800, height=600)
'''
st.code(code,language='python')