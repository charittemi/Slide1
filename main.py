# streamlit >streamlit run main.py

import streamlit as st
from PIL import Image

st.title('タイトル')
st.caption('これはテスト用に作ったページです')
st.subheader('About')
st.text('streamlitでテストページを作ってみました')

image=Image.open('./imgs/amago.jpg')
st.image(image, width=250)
st.text('')

# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=800, height=600)
st.text('ok')

