import streamlit as st
import pandas as pd

def show(df):
    st.title("Análise de Sentimentos")
    
    st.write("""
    Explore a distribuição e tendências dos sentimentos em comentários no Facebook.
    """)
    
    # Espaçamento para melhor layout
    st.write('\n')
    
    # Big Numbers
    st.header("Visão Geral")
    
    col1, col2, col3 = st.beta_columns(3)
    
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

