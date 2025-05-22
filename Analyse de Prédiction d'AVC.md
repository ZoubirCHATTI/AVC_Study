# Analyse de Prédiction d'AVC

## Description
Ce projet présente une analyse exploratoire de données sur les accidents vasculaires cérébraux (AVC) à partir d'un jeu de données contenant diverses caractéristiques démographiques et médicales. L'objectif est d'explorer les facteurs de risque potentiels associés aux AVC et de préparer les données pour une future modélisation prédictive.

## Table des matières
- [Installation](#installation)
- [Structure du projet](#structure-du-projet)
- [Jeu de données](#jeu-de-données)
- [Utilisation](#utilisation)
- [Fonctionnalités](#fonctionnalités)
- [Résultats](#résultats)
- [Développements futurs](#développements-futurs)
- [Contribution](#contribution)
- [Licence](#licence)
- [Contact](#contact)

## Installation

### Prérequis
- Python 3.7+
- pip

### Configuration
1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-username/AVC_Study.git
cd AVC_Study
```

2. Installez les dépendances requises :
```bash
pip install -r requirements.txt
```

3. Téléchargez le jeu de données :
   - Option 1 : Utilisez le fichier `stroke_data.csv` fourni dans le dossier `data/`
   - Option 2 : Téléchargez le jeu de données depuis [source originale - à préciser]

## Structure du projet
```
AVC_Study/
├── data/
│   └── stroke_data.csv
├── notebooks/
│   └── AVC_Study.ipynb
├── README.md
├── requirements.txt
└── .gitignore
```

## Jeu de données
Le jeu de données contient les informations suivantes :
- `id` : Identifiant unique pour chaque patient
- `gender` : Genre du patient (Male, Female, Other)
- `age` : Âge du patient
- `hypertension` : 0 si le patient n'a pas d'hypertension, 1 si le patient a de l'hypertension
- `heart_disease` : 0 si le patient n'a pas de maladie cardiaque, 1 si le patient a une maladie cardiaque
- `ever_married` : Statut marital (Yes, No)
- `work_type` : Type d'emploi (Private, Self-employed, Govt_job, children, Never_worked)
- `Residence_type` : Type de résidence (Rural, Urban)
- `avg_glucose_level` : Niveau moyen de glucose dans le sang
- `bmi` : Indice de masse corporelle
- `smoking_status` : Statut tabagique (formerly smoked, never smoked, smokes, Unknown)
- `stroke` : 1 si le patient a eu un AVC, 0 sinon

## Utilisation
1. Ouvrez le notebook Jupyter :
```bash
jupyter notebook notebooks/AVC_Study.ipynb
```

2. Exécutez les cellules séquentiellement pour reproduire l'analyse.

3. Adaptez le chemin du fichier de données si nécessaire :
```python
# Remplacez cette ligne
df = pd.read_csv('/content/gdrive/MyDrive/FOR NEXA/Stroke_Prediction/stroke_data.csv')

# Par celle-ci
df = pd.read_csv('data/stroke_data.csv')
```

## Fonctionnalités
- Exploration et visualisation des données démographiques
- Analyse des corrélations entre les facteurs de risque et les AVC
- Traitement des valeurs manquantes
- Préparation des données pour la modélisation

## Résultats
L'analyse exploratoire révèle plusieurs facteurs potentiellement associés au risque d'AVC, notamment :
- L'âge
- L'hypertension
- Les maladies cardiaques
- Le niveau de glucose sanguin

Des visualisations détaillées sont disponibles dans le notebook.

## Développements futurs
- Implémentation de modèles prédictifs (régression logistique, random forest, etc.)
- Analyse plus approfondie des interactions entre variables
- Développement d'une application web pour la prédiction du risque d'AVC

## Contribution
Les contributions sont les bienvenues ! Pour contribuer :
1. Forkez le projet
2. Créez votre branche de fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request


## Contact
Zoubir CHATTI - email: zoubirchatti@gmail.com

