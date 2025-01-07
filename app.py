import streamlit as st
import streamlit.components.v1 as components
import os

# Configurar a página para ocupar toda a largura
st.set_page_config(layout="wide")

# Função para ler o conteúdo do arquivo HTML
def get_html_content(file_path):
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
    html_content = get_html_content(html_file)

    # Injetar CSS para remover margens e paddings padrão do Streamlit
    st.markdown("""
        <style>
        /* Remove o padding e margin padrão do Streamlit */
        .css-18e3th9 {
            padding: 0;
            margin: 0;
        }
        /* Remove o cabeçalho e o rodapé do Streamlit */
        header, footer {
            visibility: hidden;
        }
        </style>
        """, unsafe_allow_html=True)

    # Embutir o HTML no Streamlit
    components.html(
        html_content,
        height=2000,  # Ajuste conforme a altura do seu conteúdo
        width=2000,   # Ajuste conforme a largura do seu conteúdo
        scrolling=True
    )
