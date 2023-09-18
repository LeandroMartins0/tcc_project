import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

sns.set_style("whitegrid")

def plot_elbow_method(X):
    distortions = []
    K = range(1,10)
    for k in K:
        kmeanModel = KMeans(n_clusters=k)
        kmeanModel.fit(X)
        distortions.append(kmeanModel.inertia_)

    plt.figure(figsize=(10,6))
    plt.plot(K, distortions, 'bx-')
    plt.xlabel('Número de clusters')
    plt.ylabel('Distortion')
    plt.title('Método do Cotovelo mostrando o número ótimo de clusters')
    return plt

def show(df):

    st.title("📊 Clusterização de Postagens e Análise de Localização")

    st.write("""
    ### 🔍 Clusterização de Postagens

    Nesta análise, estamos usando técnicas de Machine Learning para agrupar postagens com características semelhantes em 'clusters'.
        
    **Por que clusterizar?**
        
    A clusterização nos ajuda a identificar padrões nos dados. Por exemplo, podemos encontrar grupos de postagens que têm padrões de engajamento similares ou postagens que têm reações semelhantes do público.

    **Como funciona?**

    - **Seleção de Características**: Escolhemos características das postagens, como engajamento, sentimentos e outros atributos.
    - **Normalização**: Padronizamos essas características para que tenham importância igual na análise.
    - **KMeans**: Utilizamos o algoritmo KMeans para formar os clusters.
    - **Determinação do Número de Clusters**: Usamos o 'Método do Cotovelo' para decidir o número ideal de clusters.

    Vamos mergulhar nos detalhes abaixo!
    """)


    # Preparando os dados para a clusterização
    # Selecionando colunas numéricas. Você pode adicionar ou remover de acordo com seus dados.
    cluster_data = df[['reacoes', 'curtidas', 'compartilhamentos', 'visualizacoes']]
    
    # Normalizando os dados
    scaler = StandardScaler()
    X = scaler.fit_transform(cluster_data)

    # Plotando o método do cotovelo para determinar o número de clusters
    st.subheader("Determinando o Número de Clusters")
    plt = plot_elbow_method(X)
    st.pyplot(plt.gcf())
    plt.clf()

    st.write("""
    ### 🔍 Método do Cotovelo

    O gráfico acima é conhecido como "Método do Cotovelo". Ele nos ajuda a escolher o número "ideal" de clusters. O eixo Y mostra a distorção, que diminui à medida que o número de clusters aumenta. O "cotovelo" do gráfico, ou seja, o ponto onde a taxa de diminuição começa a se nivelar, nos dá uma ideia do número ideal de clusters. Esse ponto representa um equilíbrio entre precisão e eficiência computacional.
    """)


    # Aplicando KMeans com o número de clusters escolhido (vamos supor 3 para este exemplo)
    kmeans = KMeans(n_clusters=3)
    df['cluster'] = kmeans.fit_predict(X)

    # Verificando os centróides para determinar a ordem dos clusters
    centroids = kmeans.cluster_centers_

    # Usamos os centróides para mapear os clusters. Suponhamos que a primeira coluna (reacoes) seja um bom indicador de engajamento.
    cluster_order = centroids[:, 0].argsort()

    # Mapeando os rótulos dos clusters para nomes descritivos
    cluster_mapping = {
        cluster_order[0]: 'Engajamento Baixo',
        cluster_order[1]: 'Engajamento Médio',
        cluster_order[2]: 'Engajamento Alto'
    }
    df['cluster'] = df['cluster'].map(cluster_mapping)

    # Visualizando os clusters
    st.subheader("Distribuição dos Clusters")
    cluster_counts = df['cluster'].value_counts()
    sns.barplot(x=cluster_counts.index, y=cluster_counts.values, palette="viridis")
    plt.title('Distribuição dos Clusters')
    st.pyplot(plt.gcf())
    plt.clf()


    st.write("""
    ### 🧩 O que são esses Clusters?

    Cada barra acima representa um cluster. Um cluster é um grupo de postagens que compartilham características semelhantes em termos de engajamento, sentimentos e outros parâmetros que escolhemos.

    Por exemplo:

    - **Engajamento Alto** pode representar postagens com alto engajamento e sentimentos majoritariamente positivos.
    - **Engajamento Médio** pode representar postagens com engajamento moderado e sentimentos neutros.
    - **Engajamento Baixo** pode ser postagens com baixo engajamento e sentimentos negativos.

    (Nota: As descrições acima são hipotéticas. Uma análise detalhada dos clusters reais é necessária para interpretar seu significado.)

    ### Como usamos esta informação?

    A identificação destes grupos nos permite entender melhor o comportamento e as preferências do nosso público. Podemos adaptar nosso conteúdo com base nisso ou identificar áreas que requerem mais atenção.
    """)
