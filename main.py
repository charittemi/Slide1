import streamlit as st
import streamlit.components.v1 as components

st.title('タイトル')
st.caption('これはテスト用に作ったページです')
st.subheader('About')
st.text('streamlitでテストページを作ってみました')

image = Image.open('./imgs/amago.jpg')
st.image(image, width=250)
st.text('')
st.text('ok')

# test.mdファイルをブロックで埋め込んで表示
with open('test.md', 'r', encoding='utf-8') as markdown_file:
    markdown_text = markdown_file.read()
components.html(markdown_text, width=800, height=400)
