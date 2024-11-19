import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np


filepath = "https://filedn.eu/lefeldrXcsSFgCcgc48eaLY/datasets/regression/housing-price_train.csv"
data = pd.read_csv(filepath)
data.drop("Id",axis='columns',inplace=True)
data.head()
df=data.copy()

data_numeric=data.select_dtypes(include=[np.number])
data_non_numeric=data.select_dtypes(include=[object])

st.title("Streamlit for Data Analyst")
st.dataframe(data)

st.write(f"Le dataframe est compose de {data.shape[0]} lignes et {data.shape[1]} colonnes") 

st.subheader("Preparation et nettoyage des données")

# calcul du pourcentage de valeurs null
percent_null= data.isnull().sum()*100 / len(data)
percent_null.sort_values(ascending=False,inplace=True)

#seuil de visualisation
threshold_view = int(st.text_input("Seuil de visualisation", value=2))

col1, col2 = st.columns([1, 1])
with col1:
    fig, ax = plt.subplots()
    filtered = percent_null[percent_null.values > threshold_view]
    ax = sns.barplot(x = filtered, y = filtered.index, orient='h')
    ax.set_title(f"Répartition du pourcentage de valeurs manquantessupérieures au seuil de {threshold_view}")
    st.pyplot(fig)

# afffichage des 10 premiers
with col2:
    st.write(percent_null.head(10))

# suprimer les columns superior a 70% de valeurs nulls

threshold = int(st.text_input("seuil de suppression selon le pourcentage de valeurs nulls", value=70))
columns_to_drop = percent_null[
    percent_null.values > threshold].index

st.text(f"les colonnes liste pour suppression sont: {columns_to_drop}")

if st.button("Supprimer les colonnes"):
    # le dataframe sans le columns suprimer
    data.drop(columns_to_drop, axis='columns', inplace=True)
    st.success(f"Les colonnes {list(columns_to_drop)} ont été supprimées avec succès!")
    st.write("Nouveau dataframe :", data.shape)
    st.dataframe(data)

st.subheader("Vérification des valeurs nulls")
st.write("nombre de valeurs nulls par colonne",data.isnull().sum())

st.subheader("Imputation des valeurs nulls")
st.write("Pour limputation des valeurs nulls, nous allons separe le dataframe en deux numeriques et non numeriques")
st.write("1. Les colonnes numeriques")

#columns numeriques

if 'data' not in st.session_state:
    st.session_state.data = data.copy()
if 'data_numeric' not in st.session_state:
    st.session_state.data_numeric = data.select_dtypes(include=[np.number]).copy()
if 'data_non_numeric' not in st.session_state:
    st.session_state.data_non_numeric = data.select_dtypes(include=[np.object_]).copy()

st.dataframe(st.session_state.data_numeric.head(5))
st.write("Dataframe avec les colonnes numeriques:", st.session_state.data_numeric.shape)

col1, col2 = st.columns(2)
with col1:
    if st.button("Imputation des colonnes avec la moyenne"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'mean')
        imputation.fit(st.session_state.data_numeric)
        st.session_state.data_numeric.loc[:, :] = imputation.transform(st.session_state.data_numeric)
with col2:
    if st.button("Imputation des colonnes avec la mediane"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'median')
        imputation.fit(st.session_state.data_numeric)
        st.session_state.data_numeric.loc[:, :] = imputation.transform(st.session_state.data_numeric)

st.dataframe(st.session_state.data_numeric.head(5))

st.write("2. Les colonnes non numeriques")
#columns non numeriques

st.dataframe(st.session_state.data_non_numeric.head(5))
st.write("Dataframe avec les colonnes numeriques:", st.session_state.data_non_numeric.shape)

if st.button("Imputation des colonnes non numeriques"):
        imputation = SimpleImputer(missing_values = np.nan, 
                           strategy = 'most_frequent')
        imputation.fit(st.session_state.data_non_numeric)
        st.session_state.data_non_numeric.loc[:, :] = imputation.transform(st.session_state.data_non_numeric)

st.dataframe(st.session_state.data_non_numeric.head(5))

#verification s'il n'y a pas de valeurs null
col1, col2 = st.columns(2)
with col1:
    st.write("Valeurs nulles dans les colonnes numériques:")
    st.write(st.session_state.data_numeric.isnull().sum())
with col2:
    st.write("Valeurs nulles dans les colonnes non numériques:")
    st.write(st.session_state.data_non_numeric.isnull().sum())

col1, col2, col3 = st.columns(3)
col1.write("This is column 1")
col2.write("This is column 2")
col3.write("This is column 2")
