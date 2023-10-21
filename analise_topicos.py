import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation as LDA
from nltk.corpus import stopwords
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from wordcloud import WordCloud

sns.set_style("whitegrid")

def show_topic_analysis(df):

    st.title("📚 Análise de Tópicos")
    
    st.write("""
    Descubra os principais tópicos discutidos nos comentários das redes sociais. Esta seção ajuda a identificar padrões e assuntos frequentes no seu público.
    """)

    # Entendendo a Análise de Tópicos
    st.write("""
    ### 🔍 Entendendo a Análise de Tópicos:

    - **📖 Tópicos**: Grupos de palavras que geralmente aparecem juntas e representam um tema específico.
    
    - **🛠️ LDA**: Técnica estatística que identifica padrões de palavras para classificar textos em tópicos.
    """)

    # Processando os tópicos
    st.header("🔎 Descobrindo os Tópicos")
    
    stop_words = stopwords.words('portuguese')
    count_vectorizer = CountVectorizer(stop_words=stop_words, max_df=0.9, min_df=2, max_features=1000)
    term_matrix = count_vectorizer.fit_transform(df['comentario'])
    
    lda = LDA(n_components=5, random_state=42)
    lda.fit(term_matrix)

    # Nomes genéricos para os tópicos
    topic_names = ["Tópico 1", "Tópico 2", "Tópico 3", "Tópico 4", "Tópico 5"]

    # Mostrando wordcloud para cada tópico
    for idx, topic in enumerate(lda.components_):
        st.write(f"### 📌 **{topic_names[idx]}**")
        cloud = WordCloud(stopwords=stop_words, background_color="white", max_words=10).generate_from_frequencies({count_vectorizer.get_feature_names_out()[i]: topic[i] for i in topic.argsort()[-10:]})
        plt.imshow(cloud, interpolation='bilinear')
        plt.axis('off')
        st.pyplot(plt.gcf())
        plt.clf()

    st.header("📊 Distribuição dos Tópicos")
    topic_values = lda.transform(term_matrix)
    df['topico'] = [topic_names[i] for i in topic_values.argmax(axis=1)]

    sns.countplot(data=df, x='topico', palette='viridis', order=topic_names)
    plt.title('Distribuição de Comentários por Tópico')
    plt.ylabel('Número de Comentários')
    plt.xlabel('Tópico')
    st.pyplot(plt.gcf())
    plt.clf()

    # Como utilizar os insights
    st.header("💼 Como Utilizar os Insights")

    st.write("""
    - **Planejamento de Conteúdo**: Identifique tópicos populares e crie conteúdo voltado para esses temas.
    
    - **Engajamento do Cliente**: Enderece preocupações ou tópicos frequentemente discutidos para melhorar o engajamento.
    
    - **Desenvolvimento de Produto**: Use feedback temático para inspirar novos recursos ou produtos.
    
    - **Estratégia de Marketing**: Ajuste as campanhas publicitárias com base nos tópicos que ressoam com sua audiência.
    
    A análise de tópicos é uma ferramenta rica. Use-a para entender as necessidades e interesses do seu público e tomar decisões informadas.
    """)

# show_topic_analysis(df)
