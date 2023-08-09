# app.py
import streamlit as st

def main():
    st.title('Meu Primeiro Aplicativo Streamlit')
    st.subheader('Este é um projeto de TCC para análise de sentimentos em postagens de redes sociais.')

    if st.button('Clique aqui'):
        st.write('Você clicou no botão!')

if __name__ == "__main__":
    main()
