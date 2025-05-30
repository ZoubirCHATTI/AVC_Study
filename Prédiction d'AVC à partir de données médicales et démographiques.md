# Prédiction d'AVC à partir de données médicales et démographiques

## Description du projet

Ce projet a pour objectif de développer des modèles de prédiction des accidents vasculaires cérébraux (AVC) en utilisant des données médicales et démographiques. Les AVC représentent une cause majeure de mortalité et d'invalidité dans le monde, et leur prédiction précoce pourrait permettre une intervention médicale plus rapide et efficace, améliorant ainsi les chances de survie et de récupération des patients.

Notre approche repose sur l'analyse de diverses caractéristiques des patients, telles que l'âge, le sexe, les antécédents médicaux (hypertension, maladies cardiaques), les habitudes de vie (tabagisme), et d'autres facteurs démographiques et médicaux. Nous avons implémenté et comparé différents algorithmes d'apprentissage automatique pour identifier le modèle offrant les meilleures performances de prédiction.

Le projet aborde également la problématique du déséquilibre des classes, courante dans les données médicales où les cas positifs (patients ayant subi un AVC) sont généralement moins nombreux que les cas négatifs. Des techniques de rééchantillonnage ont été appliquées pour améliorer la capacité des modèles à détecter correctement les cas d'AVC.

## Installation et prérequis

Pour utiliser ce projet, vous aurez besoin des bibliothèques Python suivantes :

```
numpy
pandas
matplotlib
seaborn
scikit-learn
```

Vous pouvez installer ces dépendances en utilisant pip :

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Structure du projet

Le projet est organisé en deux parties principales : des scripts Python contenant les fonctions réutilisables et des notebooks Jupyter présentant l'analyse et les résultats.

### Scripts Python

- **data_load.py** : Contient des fonctions pour charger les données depuis des fichiers CSV.
- **data_prep.py** : Implémente des fonctions pour la préparation et le prétraitement des données avant l'entraînement des modèles.
- **models.py** : Définit les modèles de classification utilisés (Régression Logistique et Random Forest).
- **evaluation.py** : Fournit des fonctions pour évaluer les performances des modèles à l'aide de rapports de classification et de matrices de confusion.
- **plot.py** : Contient diverses fonctions de visualisation pour explorer les données et présenter les résultats.

### Notebooks Jupyter

- **01_Présentation_et_inspection_visuelle.ipynb** : Introduction au jeu de données et exploration visuelle initiale pour comprendre la distribution des variables et leurs relations.
- **02_Nettoyage_des_données.ipynb** : Processus de nettoyage et de prétraitement des données, incluant le traitement des valeurs manquantes et la transformation des variables catégorielles.
- **04_RandomForestClassifier.ipynb** : Implémentation et évaluation du modèle Random Forest pour la prédiction d'AVC.
- **05_surechantillonnage_et_echantiollonnage_equilibré.ipynb** : Application de techniques de rééchantillonnage pour gérer le déséquilibre des classes dans les données.
- **LogisticRegression.ipynb** : Implémentation et évaluation du modèle de Régression Logistique pour la prédiction d'AVC.

## Utilisation

### Chargement des données

Pour charger les données à partir d'un fichier CSV :

```python
from data_load import load_csv

# Charger les données
data = load_csv('chemin/vers/votre/fichier.csv')
```

### Préparation des modèles

Pour utiliser le modèle de Régression Logistique :

```python
from models import L_R

# X : features, Y : variable cible
# test_size : proportion des données pour le test (ex: 0.2 pour 20%)
# max_ite : nombre maximum d'itérations pour la convergence
Y_predict, Y_test = L_R(X, Y, test_size=0.2, max_ite=1000)
```

Pour utiliser le modèle Random Forest :

```python
from models import R_F_C

# X : features, Y : variable cible
# test_size : proportion des données pour le test
# n_estimators : nombre d'arbres dans la forêt
# class_weight : pondération des classes (ex: 'balanced' pour gérer le déséquilibre)
Y_predict, Y_test = R_F_C(X, Y, test_size=0.2, n_estimators=100, class_weight='balanced')
```

### Évaluation des modèles

Pour évaluer les performances d'un modèle :

```python
from evaluation import cla_repo, conf_mat

# Afficher le rapport de classification
cla_repo(Y_test, Y_predict)

# Afficher la matrice de confusion
conf_mat(Y_test, Y_predict)
```

### Visualisation des données

Pour créer des visualisations :

```python
from plot import histplot, barplot, camembert, scatter

# Créer un histogramme
histplot(data, 'age', 'stroke', 'Distribution de l\'âge')

# Créer un diagramme à barres
barplot(data, 'gender', 'stroke', 'Distribution par genre')

# Créer un diagramme circulaire
camembert(data_hommes, data_femmes, 'stroke', 'Hommes', 'Femmes')

# Créer un nuage de points
scatter(data, 'age', 'avg_glucose_level', 'stroke', 'Âge', 'Niveau moyen de glucose')
```

## Méthodologie

Le projet suit une méthodologie d'apprentissage automatique classique :

1. **Exploration et compréhension des données** : Analyse des distributions, identification des relations entre variables, détection des valeurs aberrantes et manquantes.

2. **Prétraitement des données** : Nettoyage, gestion des valeurs manquantes, encodage des variables catégorielles, normalisation si nécessaire.

3. **Modélisation** : Implémentation de deux algorithmes de classification (Régression Logistique et Random Forest) avec différentes configurations.

4. **Gestion du déséquilibre des classes** : Application de techniques de rééchantillonnage pour améliorer la détection des cas positifs (AVC).

5. **Évaluation** : Utilisation de métriques adaptées aux problèmes de classification déséquilibrée (précision, rappel, F1-score) et de matrices de confusion pour une analyse détaillée des performances.

## Résultats et performances

Les modèles ont été évalués sur leur capacité à prédire correctement les cas d'AVC. En raison du déséquilibre des classes, une attention particulière a été portée au rappel (capacité à identifier correctement les cas positifs) plutôt qu'à la simple précision globale.

Le modèle Random Forest avec pondération des classes a généralement montré de meilleures performances que la Régression Logistique, notamment après l'application des techniques de rééchantillonnage. Les détails complets des performances sont disponibles dans les notebooks correspondants.

## Perspectives d'amélioration

Plusieurs pistes pourraient être explorées pour améliorer ce projet :

- Collecte de données supplémentaires pour réduire le déséquilibre naturel des classes
- Expérimentation avec d'autres algorithmes de classification (SVM, réseaux de neurones, etc.)
- Optimisation des hyperparamètres via une recherche en grille ou une validation croisée
- Intégration de nouvelles caractéristiques médicales potentiellement pertinentes
- Application de techniques d'apprentissage par transfert ou d'apprentissage semi-supervisé pour améliorer les performances avec des données limitées

## Contribution

Les contributions à ce projet sont les bienvenues. N'hésitez pas à proposer des améliorations via des pull requests ou à signaler des problèmes dans la section des issues.

## Licence

Ce projet est disponible sous licence open source. Vous êtes libre de l'utiliser, de le modifier et de le distribuer selon les termes de la licence.
