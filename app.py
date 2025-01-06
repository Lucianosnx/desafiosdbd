import streamlit as st
import streamlit.components.v1 as components

# Lê o conteúdo inteiro do seu arquivo HTML
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Exibe dentro do Streamlit
components.html(
    html_content,
    height=800,   # Ajuste a altura que você preferir
    width=None,   # Se quiser definir uma largura específica, pode passar aqui
    scrolling=True
)
