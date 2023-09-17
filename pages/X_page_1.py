

# streamlit >streamlit run main.py


import streamlit as st
from PIL import Image

st.title('Page 1')
st.caption('')
st.subheader('作成')

st.text('')
st.text('')

col1,col2=st.columns([1,2]) # カラムの比率1:2で設定
with col1:
    st.text('カラム１')
    
with col2:
    st.text('カラム２')

markdown = """
# タイトル
## ヘッダ

### 数式インライン表示 

$f(x) = x^2 + 1$

$(1 + 2) \times 3 - 4 \div 2 = 7$

$\displaystyle\frac{x}{y}$

$x^2$

$\displaystyle\lim_{a\to 0}f(x + a)$
<br>

### ブロック表示
$$f(x) = x^2 + 1$$

"""
st.markdown(markdown)

    #コード表示用
code='''
'''
st.code(code,language='python')
