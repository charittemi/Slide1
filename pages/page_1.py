

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


    
    
    #コード表示用
code='''

'''
st.code(code,language='python')
