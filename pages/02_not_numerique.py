import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np
import app as app

st.subheader("Imputation de valeurs du tableau non numerique")
st.write("1. Les colonnes non numeriques")

if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = app.data_non_numeric.select_dtypes(include=[np.object]).copy()
#columns numeriques

st.dataframe(st.session_state.data_non_numeric.head(5))
st.write("Dataframe avec les colonnes non numeriques:", st.session_state.data_non_numeric.shape)

st.subheader("Les valeurs nulls presente dans le dataframe")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_non_numeric.isnull().sum())

if st.button("Imputation des colonnes non numeriques"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'most_frequent')
        imputation.fit(st.session_state.data_non_numeric)
        st.session_state.data_non_numeric.loc[:, :] = imputation.transform(st.session_state.data_non_numeric)

st.dataframe(st.session_state.data_non_numeric.head(5))

st.subheader("Les valeurs nulls presente apres de imputation dans le dataframe")
st.write("nombre de valeurs nulls par colonne",st.session_state.data_non_numeric.isnull().sum())
