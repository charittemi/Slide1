# streamlit >streamlit run main.py

import streamlit as st
from PIL import Image

st.title('タイトル')
st.caption('これはテスト用に作ったページです')
st.subheader('About')
st.text('streamlitでテストページを作ってみました')

image=Image.open('./img/amago.jpg')
st.image(image, width=250)
st.text('')


st.text('ok')

