import streamlit as st
import streamlit.components.v1 as components
import os

# Configurar a página para layout wide (ocupando toda a largura da tela)
st.set_page_config(layout="wide")

# Função para ler o conteúdo do arquivo HTML
def load_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

# Obter o caminho absoluto do arquivo HTML
current_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(current_dir, 'index.html')

# Verificar se o arquivo HTML existe
if not os.path.exists(html_file):
    st.error(f"O arquivo {html_file} não foi encontrado.")
else:
    # Ler o conteúdo do HTML
    html_content = load_html(html_file)

    # Embutir o HTML no Streamlit dentro de um div que ocupa toda a tela
    html_code = f"""
    <div class="full-screen-iframe">
        {html_content}
    </div>
    """

