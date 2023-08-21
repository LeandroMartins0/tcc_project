import streamlit as st
import pandas as pd
import analise_sentimentos
# Carregar dados
df = pd.read_csv('dados_ficticios.csv', delimiter=',')

st.sidebar.title("Análises de Redes Sociais")
menu = st.sidebar.selectbox(
    "Escolha uma análise", 
    ["Análise de Sentimentos", "Análise de Engajamento", "Visualizações"]
)

if menu == "Análise de Sentimentos":
    analise_sentimentos.show(df)
elif menu == "Análise de Engajamento":
    print(teste)
    #analise_engajamento.show(df)
elif menu == "Visualizações":
    print(teste)
    #visualizacoes.show(df)
