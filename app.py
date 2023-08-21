# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import os

# Carregando os dados
@st.cache
def load_data():
    try:
        # Construa o caminho do arquivo de forma dinâmica
        file_path = os.path.join(os.path.dirname(__file__), 'dados_ficticios.csv')
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return pd.DataFrame()

df = load_data()


st.write(df.head())


# Título do Dashboard
st.title("Dashboard de Análise de Sentimentos do Facebook")

# Introdução ou descrição
st.write("""
Realize análises detalhadas sobre os sentimentos dos comentários e entenda o comportamento do público no Facebook!
""")

# Big Numbers para Análise Descritiva dos Sentimentos
st.header("Análise Descritiva dos Sentimentos")

# Quantidade de comentários positivos, neutros e negativos
pos_comments = len(df[df['sentimento'] == 'positivo'])
neu_comments = len(df[df['sentimento'] == 'neutro'])
neg_comments = len(df[df['sentimento'] == 'negativo'])

st.subheader("Quantidade de Comentários")
st.write(f"Positivos: {pos_comments}")
st.write(f"Neutros: {neu_comments}")
st.write(f"Negativos: {neg_comments}")

# Média de curtidas e reações para cada tipo de sentimento
avg_likes_pos = df[df['sentimento'] == 'positivo']['curtidas'].mean()
avg_likes_neu = df[df['sentimento'] == 'neutro']['curtidas'].mean()
avg_likes_neg = df[df['sentimento'] == 'negativo']['curtidas'].mean()

st.subheader("Média de Curtidas por Sentimento")
st.write(f"Positivos: {avg_likes_pos:.2f}")
st.write(f"Neutros: {avg_likes_neu:.2f}")
st.write(f"Negativos: {avg_likes_neg:.2f}")

# Visualizações médias por tipo de sentimento
avg_views_pos = df[df['sentimento'] == 'positivo']['visualizacoes'].mean()
avg_views_neu = df[df['sentimento'] == 'neutro']['visualizacoes'].mean()
avg_views_neg = df[df['sentimento'] == 'negativo']['visualizacoes'].mean()

st.subheader("Média de Visualizações por Sentimento")
st.write(f"Positivos: {avg_views_pos:.2f}")
st.write(f"Neutros: {avg_views_neu:.2f}")
st.write(f"Negativos: {avg_views_neg:.2f}")
