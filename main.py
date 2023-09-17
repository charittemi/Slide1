# streamlit >streamlit run main.py

import streamlit as st

st.title('Slide(Marpで複数カラムレイアウトのスライド)')
st.caption('mdファイルから作成したhtmlを埋め込んでいます')
st.text('Marpで複数カラムのレイアウトにするにはカスタムCSSを別途用意する必要あり')

# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=720, height=540)
st.text('')
st.subheader('コード')
code='''
# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=720, height=540)
'''
st.code(code,language='python')
