import streamlit as st
import os

# Configura a página para o modo "wide"
st.set_page_config(layout="wide")

def main():
    # Caminho para o arquivo index.html
    html_file = "index.html"

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
