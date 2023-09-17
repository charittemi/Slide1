

# streamlit >streamlit run main.py


import streamlit as st
from PIL import Image

st.title('Page 1')
st.caption('')
st.subheader('')

st.text('')
st.text('')

col1,col2=st.columns([1,2]) # カラムの比率1:2で設定
with col1:
    st.text('')
    
with col2:
    st.text('')

markdown = """

### 数式表示 

$f(x) = x^2 + 1$

$x_2$


"""
st.markdown(markdown)
