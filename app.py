import streamlit as st
import os

# Configura a página para o modo "wide"
st.set_page_config(layout="wide")

def main():
    # Caminho para o arquivo index.html
    html_file = "index.html"

    # Injetar CSS para remover margens e paddings padrão do Streamlit e ajustar o iframe
    st.markdown("""
        <style>
        /* Remove o padding e margin padrão do Streamlit */
        .block-container {
            padding: 0;
            margin: 0;
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
            width: 100vw;
            height: 120vh;
            border: none;
            margin: 0;
            padding: 0;
        }
        </style>
        """, unsafe_allow_html=True)

    # Verifica se o arquivo existe
    if os.path.exists(html_file):
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Exibe o conteúdo HTML usando componentes do Streamlit
        st.components.v1.html(html_content, scrolling=True, height=800)
    else:
        st.error(f"O arquivo {html_file} não foi encontrado.")

if __name__ == "__main__":
    main()
