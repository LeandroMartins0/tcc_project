import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Define o estilo dos gráficos
sns.set_theme(style="whitegrid")

# Função principal para mostrar a análise de engajamento
def show(df):
    st.title("📊 Análise de Engajamento")

    st.markdown("""
    Explore os indicadores e métricas que refletem o engajamento com as postagens nas redes sociais. Esta análise oferece insights valiosos para entender o comportamento do público-alvo e otimizar as estratégias de conteúdo.
    """)

    # Visão Geral
    st.header("🔍 Visão Geral do Engajamento")

    # Criação de métricas visuais
    metrics = ["Curtidas", "Reações", "Compartilhamentos", "Visualizações"]
    col1, col2, col3, col4 = st.columns(4)
    columns_to_display = ["curtidas", "reacoes", "compartilhamentos", "visualizacoes"]
    
    for col, metric, column_name in zip([col1, col2, col3, col4], metrics, columns_to_display):
        col.metric(metric, f"{df[column_name].sum():,}")

    # Gráfico de Engajamento por Tipo de Postagem
    st.subheader("👁‍🗨 Engajamento por Tipo de Postagem")
    fig, ax = plt.subplots()
    engagement_by_type = df.groupby('tipo_postagem')[columns_to_display].sum()
    engagement_by_type.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title("Engajamento por Tipo de Postagem")
    st.pyplot(fig)

    # Gráfico de Engajamento ao Longo do Tempo
    st.subheader("⏳ Engajamento ao Longo do Tempo")
    df['data_postagem'] = pd.to_datetime(df['data_postagem'])
    engagement_over_time = df.groupby(df['data_postagem'].dt.to_period("M"))[columns_to_display[:-1]].sum()
    fig, ax = plt.subplots()
    engagement_over_time.plot(kind='line', ax=ax)
    ax.set_title("Engajamento ao Longo do Tempo")
    st.pyplot(fig)

    # Top 5 postagens mais engajadas
    st.subheader("🏆 Top 5 Postagens por Engajamento Total")
    df['engajamento_total'] = df[columns_to_display[:-1]].sum(axis=1)
    top_engaged_posts = df.nlargest(5, 'engajamento_total')[['postagem', 'engajamento_total']]
    st.dataframe(top_engaged_posts.style.format({"engajamento_total": "{:,.0f}"}))

    st.markdown("""
    ### 🚀 Impulsione o Engajamento
    Utilize estes insights para criar conteúdo mais envolvente, direcionado às preferências da sua audiência. Melhore a frequência e o timing das postagens para maximizar o alcance e a interação.
    """)

    # Final do dashboard
    st.markdown("""
    ### 🙌 Agradecimentos
    Agradecemos por utilizar nossa análise de engajamento. Estamos comprometidos em ajudar você a crescer e engajar ainda mais com seu público.
    """)

# Aqui você adicionaria a parte do carregamento e preparação dos dados antes de chamar a função show.
