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

## Résultats obtenus

- La régression logistique offre un bon rappel (recall) pour les classes 0 et 1.  
- La précision est élevée pour la classe 0, mais faible pour la classe 1.  
- Les techniques d’échantillonnage (suréchantillonnage et échantillonnage combiné) n’apportent pas d’amélioration significative.  

## Instructions pour l’utilisation

1. **Téléchargez** depuis GitHub les dossiers suivants :  
   - `Notebooks/` (vos notebooks Jupyter)  
   - `Functions/` (vos scripts/fonctions Python)  
   - `Données/` (vos fichiers CSV)  

2. **Ouvrez** le notebook que vous souhaitez exécuter (dans Google Colab, Jupyter, etc.).  

3. **Modifiez** dans le notebook la variable `path_file` correspondant au chemin des données sur votre machine ou environnement.  
   
   Par exemple, dans Google Colab, après avoir monté Google Drive, adaptez :  
   ```python
   path_file = '/content/gdrive/MyDrive/chemin_vers_le_dossier/Données/Stroke_Prediction.csv'
