import streamlit as st
import pandas as pd

# Tente carregar o arquivo CSV
try:
    df = pd.read_csv('dados_ficticios.csv', delimiter=',')
except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
    st.stop()

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

# Organizando os big numbers em colunas
cols_comments = st.beta_columns(3)

with cols_comments[0]:
    st.markdown("**Positivos**")
    st.markdown(f"<h2 style='text-align: center; color: green;'>{pos_comments}</h2>", unsafe_allow_html=True)

with cols_comments[1]:
    st.markdown("**Neutros**")
    st.markdown(f"<h2 style='text-align: center; color: gray;'>{neu_comments}</h2>", unsafe_allow_html=True)

with cols_comments[2]:
    st.markdown("**Negativos**")
    st.markdown(f"<h2 style='text-align: center; color: red;'>{neg_comments}</h2>", unsafe_allow_html=True)

# Média de curtidas para cada tipo de sentimento
avg_likes_pos = df[df['sentimento'] == 'positivo']['curtidas'].mean()
avg_likes_neu = df[df['sentimento'] == 'neutro']['curtidas'].mean()
avg_likes_neg = df[df['sentimento'] == 'negativo']['curtidas'].mean()

# Organizando as médias em colunas
cols_likes = st.beta_columns(3)

with cols_likes[0]:
    st.markdown("**Positivos**")
    st.markdown(f"<h2 style='text-align: center; color: green;'>{avg_likes_pos:.2f}</h2>", unsafe_allow_html=True)

with cols_likes[1]:
    st.markdown("**Neutros**")
    st.markdown(f"<h2 style='text-align: center; color: gray;'>{avg_likes_neu:.2f}</h2>", unsafe_allow_html=True)

with cols_likes[2]:
    st.markdown("**Negativos**")
    st.markdown(f"<h2 style='text-align: center; color: red;'>{avg_likes_neg:.2f}</h2>", unsafe_allow_html=True)

# Visualizações médias por tipo de sentimento
avg_views_pos = df[df['sentimento'] == 'positivo']['visualizacoes'].mean()
avg_views_neu = df[df['sentimento'] == 'neutro']['visualizacoes'].mean()
avg_views_neg = df[df['sentimento'] == 'negativo']['visualizacoes'].mean()

# Organizando as visualizações em colunas
cols_views = st.beta_columns(3)

with cols_views[0]:
    st.markdown("**Positivos**")
    st.markdown(f"<h2 style='text-align: center; color: green;'>{avg_views_pos:.2f}</h2>", unsafe_allow_html=True)

with cols_views[1]:
    st.markdown("**Neutros**")
    st.markdown(f"<h2 style='text-align: center; color: gray;'>{avg_views_neu:.2f}</h2>", unsafe_allow_html=True)

with cols_views[2]:
    st.markdown("**Negativos**")
    st.markdown(f"<h2 style='text-align: center; color: red;'>{avg_views_neg:.2f}</h2>", unsafe_allow_html=True)
