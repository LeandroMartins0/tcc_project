import streamlit as st
import pandas as pd

# Caminho para o arquivo CSV
path_to_csv = "C:\\Users\\LeandroAugusto\\Documents\\TCC\\Base\\dados_ficticios.csv"

# Título da Aplicação
st.title("Análise de Sentimentos no Facebook")

# Descrição
st.write("Bem-vindo à aplicação de análise de sentimentos. Aqui você pode explorar informações iniciais.")

# Lendo o arquivo CSV
data = pd.read_csv(path_to_csv)

# Exibindo as primeiras linhas
st.write("Primeiras linhas da base de dados:")
st.dataframe(data.head())

# Resumo das estatísticas
st.write("Resumo das estatísticas:")
st.dataframe(data.describe())

# Gráfico de distribuição dos sentimentos
st.write("Distribuição dos sentimentos:")
st.bar_chart(data['sentimento'].value_counts())

# Fim da análise
st.write("Mais análises e visualizações podem ser adicionadas de acordo com suas necessidades.")
