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

data_numeric=app.data_numeric
if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = data_numeric.select_dtypes(include=[np.number]).copy()

#columns numeriques

st.dataframe(st.session_state.data_numeric.head(5))
st.write("Dataframe avec les colonnes numeriques:", st.session_state.data_numeric.shape)

st.subheader("Les valeurs nulls presente dans le dataframe")
st.write("nombre de valeurs nulls par colonne",data_numeric.isnull().sum())

col1, col2 = st.columns(2)
with col1:
    if st.button("Imputation des colonnes avec la moyenne"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'mean')
        imputation.fit(st.session_state.data_numeric)
        st.session_state.data_numeric.loc[:, :] = imputation.transform(st.session_state.data_numeric)
        logging.info("Bouton 'Imputation pour moyenne' a été cliqué.")

with col2: 
    if st.button("Imputation des colonnes avec la mediane"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'median')
        imputation.fit(st.session_state.data_numeric)
        st.session_state.data_numeric.loc[:, :] = imputation.transform(st.session_state.data_numeric)
        logging.info("Bouton 'Imputation pour la Mediane' a été cliqué.")

st.dataframe(st.session_state.data_numeric.head(5))

st.subheader("Vérification des valeurs nulls")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_numeric.isnull().sum())
