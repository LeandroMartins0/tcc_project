import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import numpy as np

# Função para treinar o modelo
def train_model(df):
    df['engajamento'] = df['curtidas'] + df['reacoes']

    X = df[['visualizacoes', 'compartilhamentos']]
    y = df['engajamento']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return model, X_test, y_test, predictions, mae

# Função para calcular o erro médio absoluto
def calculate_mae(predictions, actual):
    return np.mean(np.abs(np.array(predictions) - np.array(actual)))

# Função para mostrar a análise de previsão de engajamento
def show(df):
    st.title("🤖 Análise de Engajamento com Machine Learning")
    
    st.write("## 🔍 Explicação:")

    st.write("""
    Nesta seção, aplicamos aprendizado de máquina para prever o **engajamento** de um post nas redes sociais com base em suas **visualizações** e **compartilhamentos**.
    """)

    st.write("""
    ### 🌲 O Modelo: Floresta Aleatória (Random Forest)
    Escolhemos o modelo de Floresta Aleatória por sua capacidade de lidar bem com uma variedade de dados sem a necessidade de ajuste minucioso de parâmetros.
    """)

    st.write("""
    ### 🎯 Engajamento: O Que é e Como É Calculado?
    Definimos o **engajamento** como a soma das **curtidas** e **reações** a um post. É um indicador chave de quão interativa e atraente uma postagem é para os usuários das redes sociais.
    """)

    # Treinando o modelo
    model, X_test, y_test, predictions, mae = train_model(df)

    st.write(f"📊 Erro Médio Absoluto (MAE): {mae:.2f}")
    st.write("""
        O Erro Médio Absoluto (MAE) é uma medida que representa a média das diferenças absolutas entre as previsões do nosso modelo e os valores reais. 
        Quanto menor o valor de MAE, mais precisa é a previsão.
    """)

    st.write("## 🔮 Faça sua previsão!")
    visualizacoes = st.number_input("👁️‍🗨️ Insira o número de visualizações:", step=1)
    compartilhamentos = st.number_input("🔗 Insira o número de compartilhamentos:", step=1)

    if st.button("Prever Engajamento"):
        st.write(f"Valores inseridos: Visualizações={visualizacoes}, Compartilhamentos={compartilhamentos}")
        prediction = model.predict([[visualizacoes, compartilhamentos]])
        st.write(f"🎉 Engajamento previsto: {prediction[0]:.2f}")
        st.write(f"👍 Curtidas Previstas: {int(prediction[0] * 0.6):d}")
        st.write(f"👍 Reações Previstas: {int(prediction[0] * 0.4):d}")
        st.write(f"🔗 Compartilhamentos Previstos: {int(prediction[0] * 0.2):d}")

        # Gráfico de barra com as previsões
        labels = ['Curtidas', 'Reações', 'Compartilhamentos']
        values = [int(prediction[0] * 0.6), int(prediction[0] * 0.4), int(prediction[0] * 0.2)]

        fig, ax = plt.subplots(figsize=(8, 6))
        ax.bar(labels, values, color=['blue', 'green', 'orange'])
        ax.set_ylabel('Quantidade')
        ax.set_title('Previsão de Engajamento')
        st.pyplot(fig)

# Carregando dados fictícios
data = pd.read_csv('dados_ficticios.csv', delimiter=',')
data['data_comentario'] = pd.to_datetime(data['data_comentario'])

# Mostrando a análise de previsão de engajamento
show(data)
