import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def show(df):
    st.title("Análise de Engajamento")
    
    st.write("""
    Explore os indicadores e métricas que refletem o engajamento com as postagens nas redes sociais.
    """)

    # Convertendo a coluna 'data_postagem' para datetime
    df['data_postagem'] = pd.to_datetime(df['data_postagem'], errors='coerce')
    
    # Removendo possíveis linhas com 'tipo_postagem' NaN
    df.dropna(subset=['tipo_postagem'], inplace=True)

    # Visão Geral
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
    plt.figure(figsize=(10, 6))
    engagement_by_type.plot(kind='bar', stacked=True)
    plt.title('Engajamento por Tipo de Postagem')
    plt.ylabel('Total')
    st.pyplot(plt.gcf())
    plt.clf()

    # Engajamento ao longo do tempo
    st.subheader("Engajamento ao Longo do Tempo")
    engagement_over_time = df.groupby(df['data_postagem'].dt.date).sum()[['curtidas', 'reacoes', 'compartilhamentos']]
    plt.figure(figsize=(10, 6))
    engagement_over_time.plot()
    plt.title('Engajamento ao Longo do Tempo')
    plt.ylabel('Total')
    st.pyplot(plt.gcf())
    plt.clf()

    # Top 5 postagens mais engajadas
    st.subheader("Top 5 Postagens por Engajamento Total (Curtidas + Reações + Compartilhamentos)")
    df['engajamento_total'] = df['curtidas'] + df['reacoes'] + df['compartilhamentos']
    top_engaged_posts = df.sort_values(by='engajamento_total', ascending=False).head(5)

    col_style = """
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 10px;
    """

    for _, row in top_engaged_posts.iterrows():
        
        st.markdown(f"### {row['postagem']}")
        
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
        
        st.write("---")

    st.write("""
    ### Obrigado por explorar a análise de engajamento!
    Use estes insights para otimizar suas estratégias de postagem e melhorar o engajamento.
    """)

