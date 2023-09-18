import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

def train_model(df):
    df['engajamento'] = df['curtidas'] + df['reacoes']

    X = df[['visualizacoes', 'compartilhamentos']]
    y = df['engajamento']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

    model = RandomForestRegressor(n_estimators=100, random_state=0)
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)

    return model, mae

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

    st.write("""
    ### 📉 Erro Médio Absoluto (MAE)
    O **Erro Médio Absoluto** representa a diferença média entre as previsões do nosso modelo e os valores reais. 
    Um MAE menor indica previsões mais precisas.
    """)

    # Treinando o modelo
    model, mae = train_model(df)

    st.write(f"📊 Erro Médio Absoluto da Previsão: {mae:.2f}")

    st.write("## 🔮 Faça sua previsão!")
    visualizacoes = st.number_input("👁️‍🗨️ Insira o número de visualizações:")
    compartilhamentos = st.number_input("🔗 Insira o número de compartilhamentos:")

    if st.button("Prever Engajamento"):
        prediction = model.predict([[visualizacoes, compartilhamentos]])
        st.write(f"🎉 Engajamento previsto: {prediction[0]:.2f}")
        st.write("""
        Isso significa que, com base nas visualizações e compartilhamentos fornecidos, nosso modelo prevê que este post receberá aproximadamente este número de interações (curtidas + reações) no total.
        """)
