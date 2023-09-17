# streamlit >streamlit run main.py

import streamlit as st

st.title('Main')
st.subheader('スライド作成メモ')
st.text('')

markdown = """

### Marpスライドの特徴
- Markdown記法で書いたテキストを他の形式（pptx、HTML、PDF）に出力できる
- `<!--  -->`コメントはパワポの各スライド下のメモ欄に入力される（地味に便利）
- 複数カラム（段組み）のレイアウトにするにはCSSやHTMLの作業が必要
- 画像配置はやりづらい（CSSの作業になる）
→ ただし、一度自前でテンプレートCSS作っておけば使いまわせそう
- パワポのように各スライドを直接編集できない
- スライド内のテキストをコピペできない（PDFなら可）

→ 上記特徴ゆえ、使う場面を選ぶものの、割り切ってシンプルなスライド作りたいなら便利。  
べージ別レイアウトにこだわると<div>だらけになって元mdファイルの可読性が損なわれてしまう。（Markdownの良さが損なわれる）  

"""
st.markdown(markdown)


st.text('')