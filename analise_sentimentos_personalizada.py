import streamlit as st
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_sentiment(text):
    sentiment = TextBlob(text).sentiment.polarity

    # Palavras-chave para identificar comentários
    negative_keywords = ['decepcionado', 'esperava mais', 'nada especial', 'infelizmente', 'não atendeu']
    positive_keywords = ['fantástico', 'melhor compra', 'perfeito', 'recomendar', 'amo esses produtos']
    neutral_keywords = ['talvez compre', 'preciso pensar', 'aguardar mais opiniões', 'sem expressão de sentimentos']

    # Verifica se o comentário contém alguma das palavras-chave negativas
    if any(keyword in text.lower() for keyword in negative_keywords) or sentiment < -0.05:
        return 'Negativo', sentiment
    # Verifica se o comentário contém alguma das palavras-chave positivas
    elif any(keyword in text.lower() for keyword in positive_keywords) or sentiment > 0.05:
        return 'Positivo', sentiment
    # Verifica se o comentário contém alguma das palavras-chave neutras
    elif any(keyword in text.lower() for keyword in neutral_keywords) or (sentiment >= -0.05 and sentiment <= 0.05):
        return 'Neutro', sentiment
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
        st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{pos_count}</h1>", unsafe_allow_html=True)
    with col2:
        st.markdown("**🟡 Neutro**")
        neut_count = (data['Classificação Sentimento'] == 'Neutro').sum()
        st.markdown(f"<h1 style='text-align: center; color: #999;'>{neut_count}</h1>", unsafe_allow_html=True)
    with col3:
        st.markdown("**🔴 Negativo**")
        neg_count = (data['Classificação Sentimento'] == 'Negativo').sum()
        st.markdown(f"<h1 style='text-align: center; color: #F44336;'>{neg_count}</h1>", unsafe_allow_html=True)

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

    # Detalhes dos Sentimentos
    st.header("📈 Detalhes dos Sentimentos")

    # Gráficos de barra mostrando a distribuição dos sentimentos - Cores Corrigidas
    st.subheader("📌 Distribuição dos Sentimentos")
    sentiments = data['Classificação Sentimento'].value_counts().reindex(["Positivo", "Neutro", "Negativo"])
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiments.index, y=sentiments.values, palette=["#4CAF50", "#999", "#F44336"])
    plt.title('Distribuição dos Sentimentos')
    plt.ylabel('Quantidade de Comentários')
    st.pyplot(plt.gcf())
    plt.clf()

    # Evolução dos sentimentos ao longo do tempo - Cores Corrigidas
    data['data_comentario'] = pd.to_datetime(data['data_comentario'])
    sentiment_over_time = data.groupby([data['data_comentario'].dt.date, 'Classificação Sentimento']).size().unstack().fillna(0)

    # Reordenando as colunas para corresponder à paleta de cores
    sentiment_over_time = sentiment_over_time[['Positivo', 'Neutro', 'Negativo']]

    fig, ax = plt.subplots(figsize=(10, 6))
    sentiment_over_time.plot(ax=ax, color=['#4CAF50', '#999', '#F44336'])
    ax.set_ylabel('Quantidade')
    ax.set_title('📅 Evolução dos Sentimentos ao Longo do Tempo')
    st.pyplot(fig)

    st.header("🌟 Top 5 Postagens Mais Populares")
    top_posts = data.groupby('postagem')['curtidas'].sum().nlargest(5)
    top_posts.sort_values(inplace=True)  # Organizando para gráfico horizontal

    plt.figure(figsize=(10, 6))
    sns.barplot(x=top_posts.values, y=top_posts.index, palette="viridis")
    plt.xlabel('Número de Curtidas')
    plt.ylabel('Postagem')
    plt.title('Top 5 Postagens Mais Curtidas')

    st.pyplot(plt.gcf())

    st.write("""
    ### Por que essas Postagens são Populares?
    As postagens mais populares geralmente têm conteúdo atraente, promoções, ou mensagens que ressoam fortemente com a audiência. Elas tendem a gerar mais interações, como curtidas, compartilhamentos e comentários, aumentando seu alcance e visibilidade.
    """)

    # Recomendações Simples
    st.subheader("💡 Recomendações")
    st.write("Avalie os comentários positivos e neutralize os negativos para reforçar os aspectos que estão bem recebidos e abordar as críticas construtivas.")
    
    # Final do dashboard com um call-to-action ou uma nota.
    st.write("""
    ### 🙏 Obrigado por explorar a análise de sentimentos!
    Use esses insights para informar sua estratégia de marketing e construir uma conexão mais forte com sua audiência.
    """)
