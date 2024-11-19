import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import app as app

st.subheader("Concatener les dataframe")

if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = app.data_numeric.copy()  # Récupérer les données numériques

if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = app.data_non_numeric.copy()  # Récupérer les données non numériques

# Titre de l'application
st.subheader("concateneation du dataframe y exportation en archivo csv 📊")

st.subheader("dataframe numerique")
st.dataframe(st.session_state.data_numeric)

st.subheader("dataframe non numerique")
st.dataframe(st.session_state.data_non_numeric)

#st.subheader("dataframe numerique")

if st.button("Concatener les DataFrame"):

# le dataframe sans le columns suprimer
    if colonnes_disponibles:
        st.session_state.data_numeric.drop(colonnes_select, axis='columns', inplace=True)
        st.success(f"Les colonnes {list(colonnes_select)} ont été supprimées avec succès!")
    else:
        st.warning("Aucune colonne sélectionnée pour la suppression.")

