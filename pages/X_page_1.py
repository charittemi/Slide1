

# streamlit >streamlit run main.py


import streamlit as st
from PIL import Image

st.title('Markdownで数式を書く')
st.caption('')

st.text('ヒント：文字列の先頭にrをつける(markdown = r)ことで、pythonのraw stringとして扱われる')

st.subheader('Samples')
st.text('')

col1,col2=st.columns([1,2]) # カラムの比率1:2で設定
with col1:
    markdown = r"""

    ##### 表示結果

    $f(x) = x^2 + 1$

    $y = (1 + x) - 4x \div 2$

    $x^2$

    $\displaystyle\lim_{a \to 0}f(x + a)$

    """
    st.markdown(markdown)
st.text('')
    
with col2:

    markdown = r"""

    ##### 実際の入力
    ```
    $f(x) = x^2 + 1$

    $y = (1 + x) - 4x \div 2$

    $x^2$

    $\displaystyle\lim_{a \to 0}f(x + a)$
    ```
    
    """
    st.markdown(markdown)


    st.text('')


