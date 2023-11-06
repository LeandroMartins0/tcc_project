import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Definir o estilo do Seaborn
sns.set_style("whitegrid")

# Função principal para mostrar a análise de engajamento
def show(df):
    st.title("Análise de Engajamento")
    
    st.write("""
    Explore os indicadores e métricas que refletem o engajamento com as postagens nas redes sociais.
    """)
    
    # Visão Geral
    st.header("Visão Geral")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("<div style='text-align: center;'><h2>Curtidas</h2></div>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center;'>{df['curtidas'].sum()}</h1>", unsafe_allow_html=True)
        
    with col2:
        st.markdown("<div style='text-align: center;'><h2>Reações</h2></div>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center;'>{df['reacoes'].sum()}</h1>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div style='text-align: center;'><h2>Compartilhamentos</h2></div>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center;'>{df['compartilhamentos'].sum()}</h1>", unsafe_allow_html=True)
    
    with col4:
        st.markdown("<div style='text-align: center;'><h2>Visualizações</h2></div>", unsafe_allow_html=True)
        st.markdown(f"<h1 style='text-align: center;'>{df['visualizacoes'].sum()}</h1>", unsafe_allow_html=True)

    # Gráfico de Engajamento por Tipo de Postagem
    st.subheader("Engajamento por Tipo de Postagem")
    columns_to_sum = ['curtidas', 'reacoes', 'compartilhamentos', 'visualizacoes']
    engagement_by_type = df.groupby('tipo_postagem')[columns_to_sum].sum()
    plt.figure(figsize=(10, 6))
    engagement_by_type.plot(kind='bar', stacked=True)
    plt.title('Engajamento por Tipo de Postagem')
    plt.ylabel('Total')
    st.pyplot(plt.gcf())
    plt.clf()

    # Gráfico de Engajamento ao Longo do Tempo
    st.subheader("Engajamento ao Longo do Tempo")
    df['data_postagem'] = pd.to_datetime(df['data_postagem'])
    engagement_over_time = df.groupby(df['data_postagem'].dt.date)[columns_to_sum[:-1]].sum()
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
        
        st.markdown(f"<h2 style='text-align: center;'>{row['postagem']}</h2>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"<div style='{col_style}'><h3>Curtidas</h3><h1>{row['curtidas']}</h1></div>", unsafe_allow_html=True)
            
        with col2:
            st.markdown(f"<div style='{col_style}'><h3>Compartilhamentos</h3><h1>{row['compartilhamentos']}</h1></div>", unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"<div style='{col_style}'><h3>Visualizações</h3><h1>{row['visualizacoes']}</h1></div>", unsafe_allow_html=True)
        
        st.write("---")

    st.write("""
    ### Obrigado por explorar a análise de engajamento!
    Use estes insights para otimizar suas estratégias de postagem e melhorar o engajamento.
    """)

# Exemplo de uso
if __name__ == '__main__':
    # Carregar dados de exemplo
    data = {
        'postagem': ['Postagem 1', 'Postagem 2', 'Postagem 3', 'Postagem 4', 'Postagem 5'],
        'curtidas': [100, 200, 150, 300, 250],
        'reacoes': [50, 80, 60, 120, 100],
        'compartilhamentos': [30, 40, 35, 70, 60],
        'visualizacoes': [1000, 1500, 1200, 2000, 1800],
        'tipo_postagem': ['Texto', 'Imagem', 'Vídeo', 'Imagem', 'Vídeo']
    }
    df = pd.DataFrame(data)
    
    show(df)
