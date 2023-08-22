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
    st.sidebar.subheader("Filtros")
    
    # Convertendo a coluna de data para o tipo correto
    df['data_comentario'] = pd.to_datetime(df['data_comentario'])
    
    # Filtro por data
    start_date = st.sidebar.date_input("Data de início", df['data_comentario'].min().date())
    end_date = st.sidebar.date_input("Data final", df['data_comentario'].max().date())
    
    if start_date > end_date:
        st.sidebar.error('Erro: Data de início deve ser anterior à data final.')
    else:
        df = df[(df['data_comentario'].dt.date >= start_date) & (df['data_comentario'].dt.date <= end_date)]
    
    # Filtro por tipo de postagem
    unique_types = sorted(df['tipo_postagem'].dropna().unique())
    selected_types = st.sidebar.multiselect("Selecione os tipos de postagem", unique_types, default=unique_types)
    df = df[df['tipo_postagem'].isin(selected_types)]
    
    # Filtro por localização
    unique_locations = sorted(df['localizacao'].dropna().unique())
    selected_locations = st.sidebar.multiselect("Selecione as localizações", unique_locations, default=unique_locations)
    df = df[df['localizacao'].isin(selected_locations)]
    
    # Filtro por língua
    unique_languages = sorted(df['lingua'].dropna().unique())
    selected_languages = st.sidebar.multiselect("Selecione as línguas", unique_languages, default=unique_languages)
    df = df[df['lingua'].isin(selected_languages)]

    analise_sentimentos.show(df)
elif menu == "Análise de Engajamento":
    print("teste")
    #analise_engajamento.show(df)
elif menu == "Visualizações":
    print("teste")
    #visualizacoes.show(df)
