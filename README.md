# Project 7 - Création d'un Dashboard - OpenClassrooms
Elena Nardi, Avril 2023

## URL app
https://elena-openclassrooms-predict.herokuapp.com/

## General purposes.
Ce depot contient une application à des fins éducatives et répondant au concours Kaggle :
"Risque de défaut de crédit à domicile" (https://www.kaggle.com/c/home-credit-default-risk)

L'objectif principal de cette application est de prédire la probabilité de remboursement d'un crédit.


## Implementation.

Cette application a été implémentée à l'aide du framework Flask et codé en Python. Les packages nécessaires pour exécuter cette application sont répertoriés dans le fichier requirements.txt. L'application principale app.py est accompagnée des éléments suivants :
 - tests unitaires dans le dossier tests
 - model.pkl, fichier qui contient le modèle de prédiction ; le package pickle a été utilisé pour exporter le modèle après optimisation et entrainement
 - les fichiers Procfile et runtime.txt pour le déploiement sur Heroku
 - test_kaggle_reduced.csv, fichier des données d'entrée du modèle




