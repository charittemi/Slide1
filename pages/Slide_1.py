﻿
import streamlit as st

st.title('Slide')
st.subheader('')
st.text('')

# Slide1.htmlを埋め込む
with open('Slide1.html', 'r', encoding='utf-8') as html_file:
    slide_html = html_file.read()

st.components.v1.html(slide_html, width=720, height=540)
st.text('')