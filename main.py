﻿# Local URL: http://localhost:8501
# Network URL: http://192.168.0.24:8501

# streamlit >streamlit run main.py


import streamlit as st
from PIL import Image

st.title('タイトル')
st.caption('これはスライド用に作ったページです')
st.subheader('About')
st.text('Marpスライド')

st.text('')
image=Image.open('amago.jpg')
st.image(image, width=250)
st.text('')

<iframe src="http://localhost:8501/path/to/test.md" width="100%" height="500"></iframe>
st.text('okok')

