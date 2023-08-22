import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def show(df):
    st.title("Análise de Sentimentos")
    
    st.write("""
    Explore a distribuição e tendências dos sentimentos em comentários no Facebook.
    """)

    # Entendendo os Sentimentos
    st.write("""
    ### Entendendo os Sentimentos:
    
    - **Positivo**: Comentários que expressam uma avaliação ou reação favorável a postagens, sugerindo satisfação, alegria ou outros sentimentos benéficos.
    
    - **Neutro**: Comentários que não expressam sentimentos fortes ou claros em qualquer direção. Geralmente são observacionais, factuais ou não carregam um tom emocional evidente.
    
    - **Negativo**: Comentários que expressam desagrado, insatisfação, tristeza ou outros sentimentos indesejáveis.
    
    Estes sentimentos são inferidos automaticamente pela API do Facebook com base no conteúdo dos comentários.
    """)

    # Big Numbers
    st.header("Visão Geral")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**Positivo**")
        st.markdown(f"<h1 style='text-align: center; color: green;'>{len(df[df['sentimento'] == 'positivo'])}</h1>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("**Neutro**")
        st.markdown(f"<h1 style='text-align: center; color: gray;'>{len(df[df['sentimento'] == 'neutro'])}</h1>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("**Negativo**")
        st.markdown(f"<h1 style='text-align: center; color: red;'>{len(df[df['sentimento'] == 'negativo'])}</h1>", unsafe_allow_html=True)

    st.header("Detalhes dos Sentimentos")

    # Gráficos de barra mostrando a distribuição dos sentimentos
    st.subheader("Distribuição dos Sentimentos")
    sentiments = df['sentimento'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(sentiments.index, sentiments.values, palette=["red", "gray", "green"])
    plt.title('Distribuição dos Sentimentos')
    plt.ylabel('Quantidade de Comentários')
    st.pyplot(plt.gcf())
    plt.clf()

    # Evolução dos sentimentos ao longo do tempo
    df['data_comentario'] = pd.to_datetime(df['data_comentario'])
    sentiment_over_time = df.groupby([df['data_comentario'].dt.date, 'sentimento']).size().unstack().fillna(0)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sentiment_over_time.plot(ax=ax, color=['green', 'gray', 'red'])
    ax.set_ylabel('Quantidade')
    ax.set_title('Evolução dos Sentimentos ao Longo do Tempo')
    st.pyplot(fig)

    # Reações e curtidas por sentimento
    st.subheader("Reações e Curtidas por Sentimento")
    reactions_avg = df.groupby('sentimento')[['reacoes', 'curtidas']].mean()
    reactions_avg.plot(kind='bar', figsize=(10, 6), color=['blue', 'yellow'])
    plt.title('Reações e Curtidas por Sentimento')
    plt.ylabel('Média de Reações/Curtidas')
    st.pyplot(plt.gcf())
    plt.clf()

    # Distribuição de postagens por tipo
    st.subheader("Distribuição de Postagens por Tipo")
    post_type_counts = df['tipo_postagem'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(post_type_counts.index, post_type_counts.values, palette="viridis")
    plt.title('Distribuição de Postagens por Tipo')
    plt.ylabel('Número de Postagens')
    st.pyplot(plt.gcf())
    plt.clf()

    st.subheader("Top 5 postagens por curtidas")
    top_posts = df.sort_values(by='curtidas', ascending=False).head(5)

    for _, row in top_posts.iterrows():
        card_content = f"""
        <div style="border: 1px solid #E0E0E0; border-radius: 5px; padding: 20px; margin-bottom: 20px;">
            <h4 style="color: #333; margin-bottom: 20px;">{row['postagem']}</h4>
            <div style="display: flex; justify-content: space-between;">
                <div><strong>Curtidas:</strong> {row['curtidas']}</div>
                <div><strong>Compartilhamentos:</strong> {row['compartilhamentos']}</div>
                <div><strong>Visualizações:</strong> {row['visualizacoes']}</div>
            </div>
        </div>
        """
        st.markdown(card_content, unsafe_allow_html=True)

    # Final do dashboard com um call-to-action ou uma nota.
    st.write("""
    ### Obrigado por explorar a análise de sentimentos!
    Mantenha-se atualizado e tome decisões baseadas em dados.
    """)
