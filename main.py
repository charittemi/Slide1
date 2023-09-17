# streamlit >streamlit run main.py

import streamlit as st

st.title('タイトル')
st.caption('これはスライド表示確認用に作ったページです')
st.subheader('About')
st.text('streamlitを使って作成し、スライドのhtmlを埋め込んでいます')

st.text('')

# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=800, height=600)
st.text('ok')

code='''
# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=800, height=600)
'''
st.code(code,language='python')