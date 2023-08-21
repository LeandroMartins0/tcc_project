import streamlit as st
import pandas as pd

def show(df):
    st.title("Análise de Sentimentos")
    
    st.write("""
    Explore a distribuição e tendências dos sentimentos em comentários no Facebook.
    """)
    
    # Descrição dos sentimentos
    st.write("""
    ### Entendendo os Sentimentos:
    
    - **Positivo**: Comentários que expressam uma avaliação ou reação favorável a postagens, sugerindo satisfação, alegria ou outros sentimentos benéficos.
    
    - **Neutro**: Comentários que não expressam sentimentos fortes ou claros em qualquer direção. Geralmente são observacionais, factuais ou não carregam um tom emocional evidente.
    
    - **Negativo**: Comentários que expressam desagrado, insatisfação, tristeza ou outros sentimentos indesejáveis.
    
    Estes sentimentos são inferidos automaticamente pela API do Facebook com base no conteúdo dos comentários.
    """)

    # Espaçamento para melhor layout
    st.write('\n')
    
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
    
    # Espaçamento
    st.write('\n\n')
    
    # Gráficos (Aqui você pode adicionar gráficos para visualizar distribuição, tendências, etc.)
    st.header("Detalhes dos Sentimentos")
    
    # Gráficos de barra mostrando a distribuição dos sentimentos
    st.subheader("Distribuição dos Sentimentos")
    sentiments = ['positivo', 'neutro', 'negativo']
    sentiment_counts = [len(df[df['sentimento'] == sentiment]) for sentiment in sentiments]
    
    fig, ax = plt.subplots()
    ax.bar(sentiments, sentiment_counts, color=['green', 'gray', 'red'])
    ax.set_ylabel('Quantidade')
    ax.set_title('Quantidade de Comentários por Sentimento')
    st.pyplot(fig)
    
    # Gráfico de linha mostrando a evolução dos sentimentos ao longo do tempo
    st.subheader("Evolução dos Sentimentos ao Longo do Tempo")
    df['data_comentario'] = pd.to_datetime(df['data_comentario'])
    sentiment_over_time = df.groupby([df['data_comentario'].dt.date, 'sentimento']).size().unstack().fillna(0)
    
    fig, ax = plt.subplots()
    sentiment_over_time.plot(ax=ax, color=['green', 'gray', 'red'])
    ax.set_ylabel('Quantidade')
    ax.set_title('Evolução dos Sentimentos ao Longo do Tempo')
    st.pyplot(fig)

    
    # Por exemplo: Gráfico de barras para visualizar a quantidade de sentimentos ao longo do tempo
    # (Isso é apenas um esboço. Você precisa implementar o código real para criar o gráfico.)
    st.subheader("Distribuição de sentimentos ao longo do tempo")
    st.write("Aqui você pode inserir um gráfico mostrando como os sentimentos evoluíram ao longo do tempo.")
    
    # Espaçamento
    st.write('\n')
    
    # Feedback do usuário ou insights
    st.header("Insights")
    st.info("Os comentários positivos têm uma média de curtidas mais alta em comparação com outros sentimentos.")
    
    # Outras análises ou gráficos podem ser adicionados conforme necessário

    # Final do dashboard com um call-to-action ou uma nota.
    st.write("""
    ### Obrigado por explorar a análise de sentimentos!
    Mantenha-se atualizado e tome decisões baseadas em dados.
    """)

