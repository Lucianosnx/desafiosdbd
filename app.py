import streamlit as st
import streamlit.components.v1 as components
import os

# Configurar a página para layout wide (ocupando toda a largura da tela)
st.set_page_config(layout="wide")

# Função para ler o conteúdo do arquivo HTML
def get_html_content(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Obter o caminho absoluto do arquivo HTML
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(current_dir, 'index.html')
html_content = get_html_content(html_file)

# Embutir o HTML no Streamlit
components.html(html_content, height=2000, width=2000, scrolling=True)
