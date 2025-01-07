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

    # Injetar CSS para remover margens e paddings padrão do Streamlit e ajustar o iframe
    st.markdown("""
        <style>
        /* Remove o padding e margin padrão do Streamlit */
        .block-container {
            padding: 0;
            margin: 0;
            height: 100vh;
            width: 100vw;
        }
        /* Remove o cabeçalho e o rodapé do Streamlit */
        header, footer {
            visibility: hidden;
        }
        /* Ajusta o iframe para ocupar toda a tela */
        .full-screen-iframe {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
            margin: 0;
            padding: 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # Embutir o HTML no Streamlit dentro de um div que ocupa toda a tela
    html_code = f"""
    <div class="full-screen-iframe">
        {html_content}
    </div>
    """

    # Determinar uma altura e largura suficientemente grande para acomodar diferentes tamanhos de tela
    # Como Streamlit requer valores numéricos, usamos um valor alto e confiamos no CSS para ajustar
    components.html(
        html_code,
        scrolling=False  # Desativa a rolagem do iframe
    )
