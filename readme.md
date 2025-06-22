# Analyse de Prédiction d’AVC

## Description  
Ce projet vise à analyser et prédire le risque d’AVC (Accident Vasculaire Cérébral) à partir de données patients.  
Il contient plusieurs notebooks permettant l’inspection des données, le nettoyage, ainsi que l’application de modèles de régression logistique, avec et sans suréchantillonnage.  

## Structure du projet

- `Notebooks/` : notebooks Jupyter contenant les différentes étapes d’analyse  
- `Functions/` : scripts Python regroupant les fonctions utilisées dans les notebooks  
- `Données/` : fichiers CSV des données utilisées  
- `Figures/` : graphiques générés (histogrammes, barres) sur les variables  

## Fichiers principaux des données

- `Stroke_Prediction.csv` : données brutes pour la prédiction d’AVC  
- `Xscaled.csv` : variables standardisées  
- `Y.csv` : variable cible (stroke ou non-stroke)
## Exécution
Pour l'exécution du fichier 01_Présentation_et_inspection_visuelle.ipynb :
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ZoubirCHATTI/AVC_Study/main?urlpath=%2Fdoc%2Ftree%2FNotebooks%2F01_Pr%C3%A9sentation_et_inspection_visuelle.ipynb)

Pour l'exécution du fichier 02_Nettoyage_des_données.ipynb :
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ZoubirCHATTI/AVC_Study/main?filepath=Notebooks/02_Nettoyage_des_données.ipynb)

Pour l'exécution du fichier 03_LogisticRegression.ipynb:
[![Binder](https://mybinder.org/badge_logo.svg)](https://hub.2i2c.mybinder.org/user/zoubirchatti-avc_study-lf0mp1u4/doc/tree/Notebooks/03_LogisticRegression.ipynb)


Pour l'exécution du fichier 04_RandomForestClassifier.ipynb:
[![Binder](https://mybinder.org/badge_logo.svg)](https://hub.2i2c.mybinder.org/user/zoubirchatti-avc_study-l0l17n17/doc/tree/Notebooks/04_RandomForestClassifier.ipynb)

Pour l'exécution du fichier 05_surechantillonnage_et_echantiollonnage_equilibré.ipynb:
[![Binder](https://mybinder.org/badge_logo.svg)](https://hub.2i2c.mybinder.org/user/zoubirchatti-avc_study-yrurc6p5/doc/tree/Notebooks/05_surechantillonnage_et_echantiollonnage_equilibr%C3%A9.ipynb)


## Résultats obtenus

- La régression logistique offre un bon rappel (recall) pour les classes 0 et 1.  
- La précision est élevée pour la classe 0, mais faible pour la classe 1.  
- Les techniques d’échantillonnage (suréchantillonnage et échantillonnage combiné) n’apportent pas d’amélioration significative.  

## Instructions pour l’utilisation

01-Lancez un notebook directement en cliquant sur l’un des badges Binder ci-dessous.
Cela ouvrira un environnement JupyterLab en ligne, sans besoin d’installation locale.

02-Explorez les notebooks situés dans le dossier Notebooks/.
Les scripts utilisés sont dans le dossier Functions/ et les données dans Données/.

Assurez-vous que la variable path_file dans chaque notebook pointe vers le bon chemin relatif, généralement:
path_file = '../Données/Stroke_Prediction.csv'
