import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.impute import SimpleImputer
import numpy as np
import logging
import io

#log_stream = io.StringIO()
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler("app.log"), logging.StreamHandler()]
)

if 'data' not in st.session_state:
    st.session_state.data = None

# Página para cargar datos
def upload_page():
    upload_option = st.radio("Choisissez une option :", 
                             ("Télécharger un fichier CSV", "Entrer une URL"))

    if upload_option == "Télécharger un fichier CSV":
        uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
        if uploaded_file is not None:
            try:
                data = pd.read_csv(uploaded_file, encoding='latin-1')
                st.session_state.data = data  # Guarda los datos en el estado
                logging.info(f"Fichier '{uploaded_file.name}' chargé avec succès.")
                
                st.subheader("Aperçu des données")
                st.dataframe(data.head())  # Mostrar los primeros registros
            except Exception as e:
                logging.error(f"Erreur lors du chargement du fichier : {e}")
                st.error("Erreur lors du chargement du fichier. Veuillez vérifier le format du fichier.")

    elif upload_option == "Entrer une URL":
        url = st.text_input("Entrez l'URL du fichier CSV")
        if st.button("Charger le fichier depuis l'URL"):
            if url:
                try:
                    data = pd.read_csv(url, encoding='latin-1')
                    st.session_state.data = data  # Guarda los datos en el estado
                    logging.info(f"Fichier à partir de l'URL '{url}' chargé avec succès.")
                    st.subheader("Aperçu des données")
                    st.dataframe(data.head())  # Mostrar los primeros registros
                except Exception as e:
                    logging.error(f"Erreur lors du chargement du fichier depuis l'URL : {e}")
                    st.error("Erreur lors du chargement du fichier. Veuillez vérifier l'URL.")
            else:
                st.warning("Veuillez entrer une URL valide.")
upload_page()
# filepath = "https://filedn.eu/lefeldrXcsSFgCcgc48eaLY/datasets/regression/housing-price_train.csv"
# data = pd.read_csv(filepath)
# data.drop("Id",axis='columns',inplace=True)


# Vérifier si les données sont déjà dans session_state
# if 'data' not in st.session_state:
#     st.session_state.data = None

#@st.cache_data

st.session_state.data_numeric=st.session_state.data.select_dtypes(include=[np.number])
st.session_state.data_non_numeric=st.session_state.data.select_dtypes(include=[object])

st.title("Streamlit for Data Analyst")
st.dataframe(st.session_state.data)

st.write(f"Le dataframe est compose de {st.session_state.data.shape[0]} lignes et {st.session_state.data.shape[1]} colonnes") 

st.subheader("Preparation et nettoyage des données")
# calcul du pourcentage de valeurs null
percent_null= st.session_state.data.isnull().sum()*100 / len(st.session_state.data)
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
    st.session_state.data.drop(columns_to_drop, axis='columns', inplace=True)
    st.success(f"Les colonnes {list(columns_to_drop)} ont été supprimées avec succès!")
    st.write("Nouveau dataframe :", st.session_state.data.shape)
    st.dataframe(st.session_state.data)
    logging.info("Bouton 'supprimer les colonnes' a été cliqué.")

st.subheader("Vérification des valeurs nulls")
st.write("nombre de valeurs nulls par colonne",st.session_state.data.isnull().sum())
