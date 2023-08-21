import streamlit as st
import pandas as pd

# Carregando os dados
@st.cache
def load_data():
    try:
        data = pd.read_csv('dados_ficticios.csv')
        return data
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")

df = load_data()

# Título do Dashboard
st.title("Dashboard de Análise de Sentimentos no Facebook")

# Subtítulo
st.subheader("Análise Descritiva dos Sentimentos")

# Calculando estatísticas
pos_comments = len(df[df['sentimento'] == 'positivo'])
neutro_comments = len(df[df['sentimento'] == 'neutro'])
neg_comments = len(df[df['sentimento'] == 'negativo'])

avg_likes_pos = df[df['sentimento'] == 'positivo']['curtidas'].mean()
avg_likes_neutro = df[df['sentimento'] == 'neutro']['curtidas'].mean()
avg_likes_neg = df[df['sentimento'] == 'negativo']['curtidas'].mean()

avg_views_pos = df[df['sentimento'] == 'positivo']['visualizacoes'].mean()
avg_views_neutro = df[df['sentimento'] == 'neutro']['visualizacoes'].mean()
avg_views_neg = df[df['sentimento'] == 'negativo']['visualizacoes'].mean()

# Exibindo Big Numbers
col1, col2, col3 = st.beta_columns(3)

with col1:
    st.markdown("**Comentários Positivos**")
    st.markdown(f"<h1 style='text-align: center; color: green;'>{pos_comments}</h1>", unsafe_allow_html=True)
    st.markdown(f"Média de curtidas: {avg_likes_pos:.2f}")
    st.markdown(f"Média de visualizações: {avg_views_pos:.2f}")

with col2:
    st.markdown("**Comentários Neutros**")
    st.markdown(f"<h1 style='text-align: center; color: gray;'>{neutro_comments}</h1>", unsafe_allow_html=True)
    st.markdown(f"Média de curtidas: {avg_likes_neutro:.2f}")
    st.markdown(f"Média de visualizações: {avg_views_neutro:.2f}")

with col3:
    st.markdown("**Comentários Negativos**")
    st.markdown(f"<h1 style='text-align: center; color: red;'>{neg_comments}</h1>", unsafe_allow_html=True)
    st.markdown(f"Média de curtidas: {avg_likes_neg:.2f}")
    st.markdown(f"Média de visualizações: {avg_views_neg:.2f}")
