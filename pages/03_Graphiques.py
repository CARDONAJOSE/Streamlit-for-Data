import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import app as app

st.subheader("Graphiques de data frame")
# Charger les données Iris

if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = app.data_numeric.copy()  # Récupérer les données numériques

if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = app.data_non_numeric.copy()  # Récupérer les données non numériques

# Titre de l'application
st.subheader("Filtrage des données non numerique avec Streamlit 📊")

# Widgets interactifs pour filtrer les colonnes à afficher
colonnes_disponibles = list(st.session_state.data_numeric.columns)
colonnes_selectionnees = st.multiselect(
    "Sélectionnez les colonnes à afficher",
    colonnes_disponibles,
    default=colonnes_disponibles
)

# Filtrer le DataFrame selon les colonnes sélectionnées
df_filtre = st.session_state.data_numeric[colonnes_selectionnees]

# Afficher le DataFrame filtré
st.dataframe(df_filtre)

def plot_all_numerique(df):
    # Filtre les columns numeriques
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        plt.figure(figsize=(14, 5))  # Taille des graphes

        # Histograme con KDE
        plt.subplot(1, 2, 1)
        sns.histplot(df[col], kde=True, bins=30, color='skyblue')
        plt.title(f'Distribution of {col} - Histogram')  # Títre específique
        plt.xlabel('')  # axis X vide
        plt.ylabel('')  # axis  Y vide

        # Boxplot
        plt.subplot(1, 2, 2)
        sns.boxplot(x=df[col], color='lightgreen')
        plt.title(f'Distribution of {col} - Boxplot')  # Títre específique
        plt.xlabel('')  # # axis X vide
        plt.ylabel('')  # # axis Y vide
        plt.suptitle(f'Distribution Analysis for {col}', fontsize=16)  # Títre general
        plt.tight_layout(rect=[0, 0, 1, 0.95])  # Ajuste l'espace du titre
        st.pyplot(plt)

if st.button("Afficher les graphiques des données non numériques"):
    plot_all_numerique(st.session_state.data_numeric)

colonnes_disponibles = list(st.session_state.data_numeric.columns)
colonnes_select = st.multiselect(
    "Sélectionnez les colonnes à afficher",
    colonnes_disponibles,
    default=[]
)
if st.button("Supprimer les colonnes"):
    # le dataframe sans le columns suprimer
    if colonnes_disponibles:
        st.session_state.data_numeric.drop(colonnes_select, axis='columns', inplace=True)
        st.success(f"Les colonnes {list(colonnes_select)} ont été supprimées avec succès!")
    else:
        st.warning("Aucune colonne sélectionnée pour la suppression.")

    st.write("Nouveau dataframe :", st.session_state.data_numeric.shape)
    st.dataframe(st.session_state.data_numeric)
