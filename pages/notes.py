import streamlit as st

# Markdownファイルのパスを指定
md_file_path = 'mdfiles\note.md'

# ファイル読み込み
with open(md_file_path, 'r') as file:
    markdown_text = file.read()

# StreamlitでMarkdownを表示します
st.markdown(markdown_text)
