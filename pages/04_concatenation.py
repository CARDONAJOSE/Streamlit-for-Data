import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import app as app
import logging

st.subheader("Concatener les dataframe et exportation en fichier csv 📊")

def init_concatenation():
    if 'data' in st.session_state and st.session_state.data is not None:
        data = st.session_state.data
        logging.info("Accès aux données numériques.")
        st.subheader("Concatene le dataframe numerique et categorique")
 # Afficher les 5 premières lignes des données numériques
    else:
        st.info("Aucune donnée chargée. Veuillez charger un fichier CSV dans la page principale.")

init_concatenation()

if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = app.data_numeric.copy()  # Récupérer les données numériques

if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = app.data_non_numeric.copy()  # Récupérer les données non numériques

# Titre de l'application

st.subheader("Dataframe numerique")
st.dataframe(st.session_state.data_numeric)

st.subheader("Dataframe non numerique")
st.dataframe(st.session_state.data_non_numeric)

# Initialiser data_concat si ce n'est pas déjà fait
if 'data_concat' not in st.session_state:
    st.session_state.data_concat = pd.DataFrame()  # Initialiser avec un DataFrame vide

# Exemple de logique de concaténation
if 'data' in st.session_state and st.session_state.data is not None:
    data = st.session_state.data

    # Logique pour concaténer des données
    if st.button("Concaténer les Données"):
        # Exemple de concaténation (ajoutez votre logique ici)
        st.session_state.data_concat = pd.concat([st.session_state.data, st.session_state.data], ignore_index=True)
        st.success("Les données ont été concaténées avec succès.")
else:
    st.warning("Aucune donnée chargée. Veuillez charger un fichier CSV dans la page principale.")

st.dataframe(st.session_state.data_concat)

if st.button("Exporter un fichier a Csv"):
    st.session_state.data_concat.to_csv('clean_data.csv')
    logging.info("Bouton 'Exporter un fichier' a été cliqué.")
else:
    st.warning("il y a un probleme")
    logging.error("Il y a un probleme en la exportation du fichier.")
