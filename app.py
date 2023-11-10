import streamlit as st
import analise_sentimentos_facebook  # Módulo para a análise de sentimentos do Facebook
import analise_sentimentos_personalizada  # Módulo para a sua análise de sentimentos personalizada
import analise_engajamento
import analise_previsao
import analise_clusterizacao
import analise_topicos
import filters
import pandas as pd
import nltk
nltk.download('stopwords')

# Função para carregar os dados
def load_data():
    data = pd.read_csv('dados_ficticios.csv', delimiter=',')
    data['data_comentario'] = pd.to_datetime(data['data_comentario'])
    return data

st.sidebar.title("Análises de Redes Sociais")
menu = st.sidebar.selectbox(
    "Escolha uma análise", 
    ["Análise de Sentimentos Geral",  # Renomeada
     "Análise de Sentimentos Marketing",  # Nova guia
     "Análise de Engajamento", 
     "Previsão de Engajamento", 
     "Análise de Clusterização",
     "Análise de Tópicos"]
)

# Filtros globais para todos os módulos
st.sidebar.subheader("Filtros")

if menu == "Análise de Sentimentos Geral":
    df = load_data()
    df = filters.apply_date_filter(df)
    df = filters.apply_post_type_filter(df)
    df = filters.apply_location_filter(df)
    df = filters.apply_language_filter(df)
    df = filters.apply_sentiment_filter(df)
    df = filters.apply_post_filter(df)
    
    analise_sentimentos_facebook.show(df)

elif menu == "Análise de Sentimentos Marketing":
    df = load_data()
    df = filters.apply_date_filter(df)
    df = filters.apply_post_type_filter(df)
    df = filters.apply_location_filter(df)
    df = filters.apply_language_filter(df)
    df = filters.apply_sentiment_filter(df)
    df = filters.apply_post_filter(df)
    
    analise_sentimentos_personalizada.show(df)

elif menu == "Análise de Engajamento":
    df = load_data()
    df = filters.apply_date_filter(df)
    df = filters.apply_post_type_filter(df)
    df = filters.apply_location_filter(df)
    df = filters.apply_language_filter(df)
    df = filters.apply_post_filter(df)
    analise_engajamento.show(df)

elif menu == "Previsão de Engajamento":
    df = load_data()
    analise_previsao.show(df)

elif menu == "Análise de Clusterização":
    df = load_data()
    df = filters.apply_date_filter(df)
    df = filters.apply_post_type_filter(df)
    df = filters.apply_location_filter(df)
    df = filters.apply_language_filter(df)
    df = filters.apply_post_filter(df)
    analise_clusterizacao.show(df)    

elif menu == "Análise de Tópicos":
    df = load_data()
    analise_topicos.show_topic_analysis(df)