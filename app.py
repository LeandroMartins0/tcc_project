import streamlit as st
import analise_sentimentos
import analise_engajamento
import analise_machine
import filters
import pandas as pd

# Carregar dados
df = pd.read_csv('dados_ficticios.csv', delimiter=',')

st.sidebar.title("Análises de Redes Sociais")
menu = st.sidebar.selectbox(
    "Escolha uma análise", 
    ["Análise de Sentimentos", 
     "Análise de Engajamento", 
     "Análise de Sentimentos Temporal", 
     "Visualizações"]
)

# Filtros globais para todos os módulos
st.sidebar.subheader("Filtros")

# Convertendo a coluna de data para o tipo correto
df['data_comentario'] = pd.to_datetime(df['data_comentario'])

df = filters.apply_date_filter(df)
df = filters.apply_post_type_filter(df)
df = filters.apply_location_filter(df)
df = filters.apply_language_filter(df)

if menu == "Análise de Sentimentos":
    df = filters.apply_sentiment_filter(df)
    analise_sentimentos.show(df)

elif menu == "Análise de Engajamento":
    analise_engajamento.show(df)

elif menu == "Análise de Sentimentos Temporal":
    analise_machine.show(df)    

elif menu == "Visualizações":
    st.error("Em desenvolvimento")
