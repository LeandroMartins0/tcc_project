import streamlit as st
import pandas as pd

# Tente carregar o arquivo CSV
try:
    df = pd.read_csv('dados_ficticios.csv', delimiter=',')
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

# Mostra as primeiras linhas do DataFrame
st.write(df.head())

# ... o restante do seu código ...
