import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np
import app as app
import logging

st.subheader("Imputation de valeurs du tableau non numerique")
st.write("1. Les colonnes non numeriques")

def not_numeric():
        if 'data' in st.session_state and st.session_state.data is not None:
                data = st.session_state.data
                logging.info("Accès aux données numériques.")
                st.subheader("Analyse des Données non Numériques")
        else:
                st.info("Aucune donnée chargée. Veuillez charger un fichier CSV dans la page principale.")
        return

# initialize les données
not_numeric()

if 'data_non_numeric' not in st.session_state:
        st.session_state.data_non_numeric=st.session_state.data.select_dtypes(include=[object])

#columns numeriques

st.dataframe(st.session_state.data_non_numeric.head(5))
st.write("Dataframe avec les colonnes non numeriques:", st.session_state.data_non_numeric.shape)

st.subheader("Les valeurs nulls presente dans le dataframe")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_non_numeric.isnull().sum())

def imputation_not_numeric():
                imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'most_frequent')
                imputation.fit(st.session_state.data_non_numeric)
                st.session_state.data_non_numeric.loc[:, :] = imputation.transform(st.session_state.data_non_numeric)
                logging.info("Bouton 'Imputation des colonnes non numeriques' a été cliqué.")

if st.button("Imputation des colonnes non numeriques"):
        imputation_not_numeric()
       
st.dataframe(st.session_state.data_non_numeric.head(5))

st.subheader("Les valeurs nulls presente apres de imputation dans le dataframe")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_non_numeric.isnull().sum())
