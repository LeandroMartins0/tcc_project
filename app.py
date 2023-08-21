# Importando as bibliotecas necessárias
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando os dados
@st.cache
def load_data():
    data = pd.read_csv('C:/Users/LeandroAugusto/Documents/TCC/Base/dados_ficticios.csv')
    return data

df = load_data()

# Título do Dashboard
st.title("Dashboard de Análise de Sentimentos")

# Introdução ou descrição
st.write("""
Realize análises detalhadas sobre os sentimentos dos comentários e entenda o comportamento do público!
""")

# Análise Descritiva dos Sentimentos
st.header("Análise Descritiva dos Sentimentos")
sent_count = df['sentimento'].value_counts()
st.bar_chart(sent_count)

# Análise Temporal
st.header("Análise Temporal")
st.write("Distribuição de sentimentos ao longo do tempo:")
df['data_comentario'] = pd.to_datetime(df['data_comentario'])
fig, ax = plt.subplots()
sns.lineplot(data=df, x='data_comentario', y='curtidas', hue='sentimento', ax=ax)
st.pyplot(fig)

# Análise de Usuários
st.header("Análise de Usuários")
most_active_users = df['usuario_comentario_id'].value_counts().head(10)
st.bar_chart(most_active_users)

# Análise de Localização
st.header("Análise de Localização")
location_count = df['localizacao'].value_counts()
st.bar_chart(location_count)

# Análise por Tipo de Postagem
st.header("Análise por Tipo de Postagem")
post_type = df['tipo_postagem'].value_counts()
st.bar_chart(post_type)

# NLP (somente placeholder, você precisa adicionar o código real)
st.header("Análise de Palavras-chave")
st.write("Aqui você pode ver as palavras-chave mais frequentes para cada sentimento.")

# Análise de Engajamento
st.header("Análise de Engajamento")
st.write("Relação entre compartilhamentos e sentimentos:")
fig, ax = plt.subplots()
sns.scatterplot(data=df, x='compartilhamentos', y='curtidas', hue='sentimento', ax=ax)
st.pyplot(fig)

# Visualizações Gráficas
st.header("Outras Visualizações")
st.write("Aqui você pode adicionar outras visualizações conforme necessário.")

# Interatividade: filtragem de data
date_range = st.slider("Selecione a faixa de datas", min_value=min(df['data_comentario']), max_value=max(df['data_comentario']), value=(min(df['data_comentario']), max(df['data_comentario']))
filtered_df = df[(df['data_comentario'] >= date_range[0]) & (df['data_comentario'] <= date_range[1])]

st.write(filtered_df)

# Aqui, você pode continuar adicionando mais funcionalidades, visualizações e análises.
