# Analyse de Fichiers CSV avec Streamlit

## Description du Projet

Ce projet est une application web interactive développée avec Streamlit, permettant aux utilisateurs de charger et d'analyser des fichiers CSV. L'application offre des fonctionnalités pour télécharger des fichiers localement ou entrer une URL pour charger des données, tout en affichant des statistiques descriptives et des visualisations des données.

## Fonctionnalités

- **Chargement de Fichiers CSV** : Les utilisateurs peuvent télécharger des fichiers CSV depuis leur ordinateur ou entrer une URL pour charger des données.
- **Aperçu des Données** : Affichage des premières lignes des données chargées pour un aperçu rapide.
- **Analyse des Données** : Possibilité d'analyser les colonnes numériques et d'afficher des statistiques descriptives.
- **Gestion des Erreurs** : Messages d'erreur clairs en cas de problème lors du chargement des fichiers.

## Technologies Utilisées

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![scikit-learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)
![Streamlit](https://img.shields.io/badge/Streamlit-%23ffffff.svg?style=for-the-badge&logo=Streamlit&logoColor=black)

**Structure de l'Application**
```bash
/mon_application
    ├── app.py # Fichier principal de l'application Streamlit
    ├── pages/ # Dossier contenant les pages supplémentaires de l'application
    │   ├── 01_numerique.py  # Page pour l'analyse des données numériques
    │   ├── 02_not_numerique.py  # Page pour l'analyse des données non numériques
    │   ├── 03_autre_page.py  # Autres pages d'analyse ou fonctionnalités supplémentaires
    │   └── 04_concatenation.py  # Page pour la concaténation de plusieurs DataFrames
    ├── assets/
    |   ├── images/                  # images du projet
    │   └── streamlit_for_data.png
    ├── tests/
    ├── requirements.txt
    ├── .gitignore
    ├── app.log
    ├── README.md
```
**Virtual environnement**
```bash
python -m venv .venv
```
> .venv is the name of the virtual environnement 

**Connect to the venv** 

- mac/linux
`source .venv/bin/activate.fish`
- windows
`.venv/Scripts/activate` or `.venv/Scripts/activate.ps1` 

**Installez les dépendances**
Assurez-vous d'avoir Python installé, puis exécutez :
```bash
pip install -r requirements.txt
```

**Quit venv**
`deactivate` 

**Lancez l'application** :
```bash
streamlit run app.py
```
## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
