import streamlit as st
import pathlib

# Ler o arquivo HTML que você postou (por exemplo, "index.html")
html_path = pathlib.Path("index.html")
html_content = html_path.read_text(encoding="utf-8")

# Usar st.components.v1.html para injetar o conteúdo
st.set_page_config(page_title="Sorteio Desafios DbD", layout="wide")

st.markdown("# Sorteio Desafios Dead By Daylight (via HTML embed)")
st.components.v1.html(html_content, height=2000, scrolling=True)
