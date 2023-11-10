import streamlit as st
import pandas as pd
from textblob import TextBlob

# Função para calcular o sentimento do comentário
def calculate_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity
    if sentiment > 0:
        return 'Positivo', sentiment
    elif sentiment < 0:
        return 'Negativo', sentiment
    else:
        return 'Neutro', sentiment

def show(data):
    st.title("🧠 Análise de Sentimentos")
    
    st.write("""
    Descubra a atmosfera e as tendências emocionais dos comentários nas redes sociais. Esta seção proporciona uma visão detalhada sobre o sentimento predominante em sua audiência.
    """)
    
    st.write("""
    ### 🔍 Como Funciona a Análise de Sentimentos:
    
    A análise de sentimentos é realizada através da biblioteca TextBlob, que avalia o texto do comentário e atribui um valor de polaridade, variando de -1 (sentimento muito negativo) a 1 (sentimento muito positivo). Comentários com polaridade acima de 0 são considerados positivos, abaixo de 0 são negativos, e com polaridade 0 são neutros.
    
    - **🟢 Positivo**: Comentários com sentimentos de alegria, satisfação ou entusiasmo.
    - **🟡 Neutro**: Comentários que são meras observações ou fatos, sem expressão de sentimentos.
    - **🔴 Negativo**: Comentários que expressam tristeza, insatisfação ou crítica.
    """)

    # Análise de Sentimento
    data['Classificação Sentimento'], data['Sentimento'] = zip(*data['comentario'].apply(calculate_sentiment))

    # Visão Geral dos Sentimentos
    st.header("📊 Visão Geral dos Sentimentos")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**🟢 Positivo**")
        pos_count = (data['Classificação Sentimento'] == 'Positivo').sum()
        st.markdown(f"<h1 style='text-align: center; color: green;'>{pos_count}</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("**🟡 Neutro**")
        neut_count = (data['Classificação Sentimento'] == 'Neutro').sum()
        st.markdown(f"<h1 style='text-align: center; color: gray;'>{neut_count}</h1>", unsafe_allow_html=True)
    with col3:
        st.markdown("**🔴 Negativo**")
        neg_count = (data['Classificação Sentimento'] == 'Negativo').sum()
        st.markdown(f"<h1 style='text-align: center; color: red;'>{neg_count}</h1>", unsafe_allow_html=True)

    # Detalhes dos Sentimentos
    st.header("📈 Detalhes dos Sentimentos")
    
    # Top Comentários Positivos
    st.subheader("🏆 Top Comentários Positivos")
    top_positive_comments = data[data['Classificação Sentimento'] == 'Positivo'].nlargest(5, 'Sentimento')['comentario']
    for comment in top_positive_comments:
        st.info(comment)
    
    # Top Comentários Neutros
    st.subheader("🔍 Top Comentários Neutros")
    top_neutral_comments = data[data['Classificação Sentimento'] == 'Neutro'].head(5)['comentario']
    for comment in top_neutral_comments:
        st.warning(comment)
    
    # Top Comentários Negativos
    st.subheader("🔻 Top Comentários Negativos")
    top_negative_comments = data[data['Classificação Sentimento'] == 'Negativo'].nsmallest(5, 'Sentimento')['comentario']
    for comment in top_negative_comments:
        st.error(comment)

    # Recomendações Simples
    st.subheader("💡 Recomendações")
    st.write("Avalie os comentários positivos e neutralize os negativos para reforçar os aspectos que estão bem recebidos e abordar as críticas construtivas.")
    
    # Final do dashboard com um call-to-action ou uma nota.
    st.write("""
    ### 🙏 Obrigado por explorar a análise de sentimentos!
    Use esses insights para informar sua estratégia de marketing e construir uma conexão mais forte com sua audiência.
    """)