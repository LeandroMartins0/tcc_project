import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

def plot_sentimento_temporal(df):
    sentiment_counts = df.groupby(['data_comentario', 'sentimento']).size().unstack().fillna(0)
    
    plt.figure(figsize=(15,7))
    for sentiment in sentiment_counts.columns:
        plt.plot(sentiment_counts.index, sentiment_counts[sentiment], label=sentiment)
    
    plt.title('Tendência de Sentimentos ao Longo do Tempo')
    plt.xlabel('Data do Comentário')
    plt.ylabel('Número de Comentários')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    return plt

def show(df):
    st.title("Análise de Engajamento e Sentimentos")
    
    # ... (mantenha todas as visualizações que você já possui no seu código) ...

    # Plot de sentimentos ao longo do tempo
    st.subheader("Análise de Sentimentos ao Longo do Tempo")
    if 'data_comentario' in df.columns and 'sentimento' in df.columns:
        plt = plot_sentimento_temporal(df)
        st.pyplot(plt.gcf())
    else:
        st.write("Os dados necessários para essa visualização não estão presentes no dataset.")
