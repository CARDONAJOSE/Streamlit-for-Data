import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import app as app
import logging

#st.subheader("Concatener les dataframe")

if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = app.data_numeric.copy()  # Récupérer les données numériques

if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = app.data_non_numeric.copy()  # Récupérer les données non numériques

# Titre de l'application
st.subheader("Concatenation du dataframe et exportation en fichier csv 📊")

st.subheader("Dataframe numerique")
st.dataframe(st.session_state.data_numeric)

st.subheader("Dataframe non numerique")
st.dataframe(st.session_state.data_non_numeric)

#st.subheader("dataframe numerique")

if st.button("Concatener les DataFrame"):
    st.session_state.data_concat= pd.concat([st.session_state.data_non_numeric, st.session_state.data_numeric], axis=1)
    logging.info("Bouton 'Concatener' a été cliqué.")
else:
    st.warning("Aucune colonne sélectionnée pour la suppression.")
    logging.error("Les DataFrames à concaténer n'existent pas.")


st.subheader("Dataframe Concatene 📊")

st.dataframe(st.session_state.data_concat)

if st.button("Exporter un fichier a Csv"):
    st.session_state.data_concat.to_csv('clean_data.csv')
    logging.info("Bouton 'Exporter un fichier' a été cliqué.")
else:
    st.warning("il y a un probleme")
    logging.error("Il y a un probleme en la exportation du fichier.")