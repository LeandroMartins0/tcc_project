# filters.py

import streamlit as st
import pandas as pd

def apply_date_filter(df):
    start_date = st.sidebar.date_input("Data de início", df['data_comentario'].min().date())
    end_date = st.sidebar.date_input("Data final", df['data_comentario'].max().date())

    if start_date > end_date:
        st.sidebar.error('Erro: Data de início deve ser anterior à data final.')
        return pd.DataFrame()

    return df[(df['data_comentario'].dt.date >= start_date) & (df['data_comentario'].dt.date <= end_date)]

def apply_post_type_filter(df):
    unique_types = sorted(df['tipo_postagem'].dropna().unique())
    selected_types = st.sidebar.multiselect("Selecione os tipos de postagem", unique_types, default=unique_types)
    return df[df['tipo_postagem'].isin(selected_types)]

def apply_location_filter(df):
    unique_locations = sorted(df['localizacao'].dropna().unique())
    selected_locations = st.sidebar.multiselect("Selecione as localizações", unique_locations, default=unique_locations)
    return df[df['localizacao'].isin(selected_locations)]

def apply_language_filter(df):
    unique_languages = sorted(df['lingua'].dropna().unique())
    selected_languages = st.sidebar.multiselect("Selecione as línguas", unique_languages, default=unique_languages)
    return df[df['lingua'].isin(selected_languages)]

def apply_sentiment_filter(df):
    unique_sentiments = sorted(df['sentimento'].dropna().unique())
    selected_sentiments = st.sidebar.multiselect("Selecione os sentimentos", unique_sentiments, default=unique_sentiments)
    return df[df['sentimento'].isin(selected_sentiments)]
