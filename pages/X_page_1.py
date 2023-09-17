

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

markdown = r"""

### 数式表示 

$f(x) = x^2 + 1$

$y = (1 + x) - 4x \div 2$

$x^2$

$\displaystyle\lim_{a \to 0}f(x + a)$

"""
st.markdown(markdown)

