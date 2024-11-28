import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np
import app as app
import logging

st.subheader("Imputation de valeurs du tableau numerique")
st.write("1. Les colonnes numeriques")

# Vérifier si les données sont dans session_state
def numerique():
    if 'data' in st.session_state and st.session_state.data is not None:
        data = st.session_state.data
        logging.info("Accès aux données numériques.")
        st.subheader("Analyse des Données Numériques")
    # Afficher les 5 premières lignes des données numériques
    else:
        st.info("Aucune donnée chargée. Veuillez charger un fichier CSV dans la page principale.")
    return

numerique()

st.session_state.data_numeric=st.session_state.data.select_dtypes(include=[np.number])
#data_numeric=app.data_numeric

#columns numeriques

def head_data():
    return st.dataframe(st.session_state.data_numeric.head(5))

head_data()
#st.dataframe(st.session_state.data_numeric.head(5))
st.write("Dataframe avec les colonnes numeriques:", st.session_state.data_numeric.shape)
st.subheader("Les valeurs nulls presente dans le dataframe")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_numeric.isnull().sum())

def imputation_moyenne():
    if st.button("Imputation des colonnes avec la moyenne"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'mean')
        imputation.fit(st.session_state.data_numeric)
        st.session_state.data_numeric.loc[:, :] = imputation.transform(st.session_state.data_numeric)
        logging.info("Bouton 'Imputation pour moyenne' a été cliqué.")

def imputation_mediane():
    if st.button("Imputation des colonnes avec la mediane"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'median')
        imputation.fit(st.session_state.data_numeric)
        st.session_state.data_numeric.loc[:, :] = imputation.transform(st.session_state.data_numeric)
        logging.info("Bouton 'Imputation pour la Mediane' a été cliqué.")

col1, col2 = st.columns(2)
with col1:
    imputation_moyenne()

with col2:
    imputation_mediane() 

head_data()
st.subheader("Vérification des valeurs nulls")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_numeric.isnull().sum())
