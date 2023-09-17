import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def show(df):
    st.title("🧠 Análise de Sentimentos")
    
    st.write("""
    Descubra a atmosfera e as tendências emocionais dos comentários nas redes sociais. Esta seção proporciona uma visão detalhada sobre o sentimento predominante em sua audiência.
    """)

    # Entendendo os Sentimentos
    st.write("""
    ### 🔍 Entendendo os Sentimentos:
    
    - **🟢 Positivo**: Comentários que exalam otimismo. Eles expressam satisfação, alegria ou outros sentimentos positivos.
    
    - **🟡 Neutro**: Comentários equilibrados. Não tendem nem para o positivo, nem para o negativo. Pense neles como observações neutras.
    
    - **🔴 Negativo**: Comentários que demonstram insatisfação ou desagrado. Eles podem indicar áreas que exigem sua atenção.
    
    Os sentimentos são determinados automaticamente pela API do Facebook com base no conteúdo dos comentários.
    """)

    # Visão Geral dos Sentimentos
    st.header("📊 Visão Geral dos Sentimentos")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("**🟢 Positivo**")
        st.markdown(f"<h1 style='text-align: center; color: green;'>{len(df[df['sentimento'] == 'positivo'])}</h1>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("**🟡 Neutro**")
        st.markdown(f"<h1 style='text-align: center; color: gray;'>{len(df[df['sentimento'] == 'neutro'])}</h1>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("**🔴 Negativo**")
        st.markdown(f"<h1 style='text-align: center; color: red;'>{len(df[df['sentimento'] == 'negativo'])}</h1>", unsafe_allow_html=True)

    st.header("📈 Detalhes dos Sentimentos")

    # Gráficos de barra mostrando a distribuição dos sentimentos
    st.subheader("📌 Distribuição dos Sentimentos")
    sentiments = df['sentimento'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=sentiments.index, y=sentiments.values, palette=["red", "gray", "green"])
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
    ax.set_title('📅 Evolução dos Sentimentos ao Longo do Tempo')
    st.pyplot(fig)

    # Reações e curtidas por sentimento
    st.subheader("👍 Reações e Curtidas por Sentimento")
    reactions_avg = df.groupby('sentimento')[['reacoes', 'curtidas']].mean()
    reactions_avg.plot(kind='bar', figsize=(10, 6), color=['blue', 'yellow'])
    plt.title('Reações e Curtidas por Sentimento')
    plt.ylabel('Média de Reações/Curtidas')
    st.pyplot(plt.gcf())
    plt.clf()

    # Distribuição de postagens por tipo
    st.subheader("🔍 Distribuição de Postagens por Tipo")
    post_type_counts = df['tipo_postagem'].value_counts()
    plt.figure(figsize=(10, 6))
    sns.barplot(x=post_type_counts.index, y=post_type_counts.values, palette="viridis")
    plt.title('Distribuição de Postagens por Tipo')
    plt.ylabel('Número de Postagens')
    st.pyplot(plt.gcf())
    plt.clf()

    st.subheader("🏆 Top 5 postagens por curtidas")

    top_posts = df.sort_values(by='curtidas', ascending=False).head(5)

    # CSS style para centralizar o conteúdo nas colunas
    col_style = """
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 10px;
    """

    for _, row in top_posts.iterrows():
        
        st.markdown(f"### {row['postagem']}")  # Tamanho de fonte um pouco maior para o título da postagem
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"<div style='{col_style}'>", unsafe_allow_html=True)
            st.markdown("👍", unsafe_allow_html=True)
            st.markdown(f"**Curtidas**<br>{row['curtidas']}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"<div style='{col_style}'>", unsafe_allow_html=True)
            st.markdown("🔄", unsafe_allow_html=True)
            st.markdown(f"**Compartilhamentos**<br>{row['compartilhamentos']}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"<div style='{col_style}'>", unsafe_allow_html=True)
            st.markdown("👁️", unsafe_allow_html=True)
            st.markdown(f"**Visualizações**<br>{row['visualizacoes']}", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")  # Separador para melhor visualização entre as postagens

    # Final do dashboard com um call-to-action ou uma nota.
    st.write("""
    ### 🙏 Obrigado por explorar a análise de sentimentos!
    Baseie suas decisões em insights e mantenha-se sempre atualizado.
    """)

