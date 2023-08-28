import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def show(df):
    st.title("Análise de Engajamento")
    
    # Visão Geral - Big Numbers
    st.header("Visão Geral")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("**Curtidas**")
        st.markdown(f"<h1 style='text-align: center;'>{df['curtidas'].sum()}</h1>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("**Reações**")
        st.markdown(f"<h1 style='text-align: center;'>{df['reacoes'].sum()}</h1>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("**Compartilhamentos**")
        st.markdown(f"<h1 style='text-align: center;'>{df['compartilhamentos'].sum()}</h1>", unsafe_allow_html=True)

    with col4:
        st.markdown("**Visualizações**")
        st.markdown(f"<h1 style='text-align: center;'>{df['visualizacoes'].sum()}</h1>", unsafe_allow_html=True)

    # Engajamento por tipo de postagem
    st.subheader("Engajamento por Tipo de Postagem")
    engagement_by_type = df.groupby('tipo_postagem').sum()[['curtidas', 'reacoes', 'compartilhamentos', 'visualizacoes']]
    engagement_by_type.plot(kind='bar', figsize=(10, 6), stacked=True)
    plt.title('Engajamento por Tipo de Postagem')
    st.pyplot(plt.gcf())
    plt.clf()

    # Engajamento ao longo do tempo
    st.subheader("Engajamento ao Longo do Tempo")
    df['data_postagem'] = pd.to_datetime(df['data_postagem'])
    engagement_over_time = df.groupby(df['data_postagem'].dt.date).sum()[['curtidas', 'reacoes', 'compartilhamentos']]
    engagement_over_time.plot(figsize=(10, 6))
    plt.title('Engajamento ao Longo do Tempo')
    st.pyplot(plt.gcf())
    plt.clf()

    # Postagens mais engajadas
    st.subheader("Top 5 postagens por engajamento total (curtidas + reações + compartilhamentos)")
    df['engajamento_total'] = df['curtidas'] + df['reacoes'] + df['compartilhamentos']
    top_engaged_posts = df.sort_values(by='engajamento_total', ascending=False).head(5)
    for _, row in top_engaged_posts.iterrows():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"**Postagem**: {row['postagem']}")
        with col2:
            st.markdown(f"**Engajamento**: {row['engajamento_total']}")
        with col3:
            st.image(row['url_imagem'] if row['url_imagem'] else row['url_video'], use_column_width=True)  # Displaying image or video thumbnail

        st.write("---")  # Separator

    st.write("""
    ### Obrigado por explorar a análise de engajamento!
    Use estes insights para otimizar suas estratégias de postagem e melhorar o engajamento.
    """)

# Para usar este módulo, importe-o em seu arquivo principal (app.py) e adicione uma nova condição para a guia de análise de engajamento.
