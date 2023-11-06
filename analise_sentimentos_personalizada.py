import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob  # Para análise de sentimento

def show(data):
    # Título
    st.title("Análise de Sentimentos")

    # Sidebar para seleção de métricas
    st.sidebar.header("Selecione as Métricas")
    show_sentiment = st.sidebar.checkbox("Análise de Sentimento")
    show_engagement = st.sidebar.checkbox("Estatísticas de Engajamento")
    show_time_series = st.sidebar.checkbox("Gráficos Temporais")
    show_post_types = st.sidebar.checkbox("Tipos de Postagem")
    show_location_language = st.sidebar.checkbox("Localização e Idioma")

    # Análise de Sentimento
    if show_sentiment:
        st.header("Análise de Sentimento")

        # Explicação
        st.markdown(
            """
            A Análise de Sentimentos avalia as emoções expressas nas postagens. Os resultados são apresentados em uma escala de -1 a 1, onde:

            - Valores próximos a 1 indicam um sentimento muito positivo.
            - Valores próximos a 0 indicam neutralidade.
            - Valores próximos a -1 indicam um sentimento muito negativo.

            Entender o sentimento pode ajudar a ajustar sua estratégia de marketing e identificar tópicos ou produtos que geram reações emocionais. 
            """
        )

        data["Sentimento"] = data["comentario"].apply(lambda x: TextBlob(str(x)).sentiment.polarity)
        fig, ax = plt.subplots()
        sns.histplot(data=data, x="Sentimento", ax=ax, kde=True)
        ax.set_title("Distribuição de Sentimentos")
        st.pyplot(fig)

        # Insights sobre sentimentos
        st.subheader("Insights sobre Sentimentos")
        sentiment_mean = data["Sentimento"].mean()
        sentiment_positive = (data["Sentimento"] > 0).sum()
        sentiment_neutral = (data["Sentimento"] == 0).sum()
        sentiment_negative = (data["Sentimento"] < 0).sum()

        st.write(f"Média de Sentimento: {sentiment_mean:.2f}")
        st.write(f"Postagens Positivas: {sentiment_positive}")
        st.write(f"Postagens Neutras: {sentiment_neutral}")
        st.write(f"Postagens Negativas: {sentiment_negative}")

    # Estatísticas de Engajamento
    if show_engagement:
        st.header("Estatísticas de Engajamento")
        engagement_stats = data[["curtidas", "reacoes", "compartilhamentos", "visualizacoes"]].sum()
        st.write("Total de Curtidas:", engagement_stats["curtidas"])
        st.write("Total de Reações:", engagement_stats["reacoes"])
        st.write("Total de Compartilhamentos:", engagement_stats["compartilhamentos"])
        st.write("Total de Visualizações:", engagement_stats["visualizacoes"])

    # Gráficos Temporais
    if show_time_series:
        st.header("Gráficos Temporais")
        data["data_postagem"] = pd.to_datetime(data["data_postagem"])
        engagement_over_time = data.groupby(data["data_postagem"].dt.date)[["curtidas", "reacoes", "compartilhamentos", "visualizacoes"]].sum()
        fig, ax = plt.subplots()
        engagement_over_time.plot(ax=ax)
        ax.set_title("Engajamento ao Longo do Tempo")
        st.pyplot(fig)

    # Tipos de Postagem
    if show_post_types:
        st.header("Tipos de Postagem")
        post_type_stats = data["tipo_postagem"].value_counts()
        st.bar_chart(post_type_stats)
        st.write("Quantidade por Tipo de Postagem:")

    # Localização e Idioma
    if show_location_language:
        st.header("Localização e Idioma")
        st.write("Top 5 Localizações:")
        top_locations = data["localizacao"].value_counts().head(5)
        st.bar_chart(top_locations)
        st.write("Top 5 Idiomas:")
        top_languages = data["lingua"].value_counts().head(5)
        st.bar_chart(top_languages)

    # Resumo Geral
    st.header("Resumo Geral")
    st.write(
        """
        Use esses insights para otimizar suas estratégias de postagem e melhorar o engajamento.
        O entendimento dos sentimentos das postagens pode ajudar a adaptar sua estratégia de marketing
        e criar conteúdo que ressoe com sua audiência.
        """
    )
