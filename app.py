import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np
import logging
import io

log_stream = io.StringIO()
logging.basicConfig(
    stream=log_stream,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

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
    logging.info("Bouton 'supprimer les colonnes' a été cliqué.")

st.subheader("Vérification des valeurs nulls")
st.write("nombre de valeurs nulls par colonne",data.isnull().sum())
