import pandas as pd
import matplotlib.pyplot as plt

def plot_sentimento_temporal(df):
    # Agregar por data e sentimento
    sentiment_counts = df.groupby(['data_comentario', 'sentimento']).size().unstack().fillna(0)
    
    # Plotar
    plt.figure(figsize=(15,7))
    for sentiment in sentiment_counts.columns:
        plt.plot(sentiment_counts.index, sentiment_counts[sentiment], label=sentiment)
    
    plt.title('Tendência de Sentimentos ao Longo do Tempo')
    plt.xlabel('Data do Comentário')
    plt.ylabel('Número de Comentários')
    plt.legend()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.tight_layout()
    plt.show()

#Para teste:

# if __name__ == "__main__":
#     df = pd.read_csv('dados_ficticios.csv', delimiter=',')
#     df['data_comentario'] = pd.to_datetime(df['data_comentario'])
#     plot_sentimento_temporal(df)
