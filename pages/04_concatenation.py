import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import app as app

#st.subheader("Concatener les dataframe")

if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = app.data_numeric.copy()  # Récupérer les données numériques

if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = app.data_non_numeric.copy()  # Récupérer les données non numériques

# Titre de l'application
st.subheader("Concatenation du dataframe et exportation en archivo csv 📊")

st.subheader("Dataframe numerique")
st.dataframe(st.session_state.data_numeric)

st.subheader("Dataframe non numerique")
st.dataframe(st.session_state.data_non_numeric)

#st.subheader("dataframe numerique")

if st.button("Concatener les DataFrame"):
    st.session_state.data_concat= pd.concat([st.session_state.data_non_numeric, st.session_state.data_numeric], axis=1)
else:
    st.warning("Aucune colonne sélectionnée pour la suppression.")

st.dataframe(st.session_state.data_concat)
