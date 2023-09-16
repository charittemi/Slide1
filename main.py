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

# iframeを埋め込む
iframe_html = """
<iframe src="http://localhost:8501/path/to/test.md" width="100%" height="1000"></iframe>
"""

st.components.v1.html(iframe_html)
st.text('okok')

