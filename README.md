### English

# Data Explorer

Data Explorer is a versatile script for exploratory data analysis, including data loading, cleaning, descriptive analysis, and visualization. Designed to be modular and reusable in various data science projects.

## Features

- **Data Loading**: Load data from CSV files.
- **Data Cleaning**: Remove duplicates and handle missing values.
- **Descriptive Analysis**: Generate descriptive statistics and correlation matrices.
- **Data Visualization**: Create histograms and heatmaps for data visualization.

## Installation

### Clone the Repository

```bash
git clone https://github.com/Tom-Souillard/data_explorer
cd data_explorer
```

### Create a Virtual Environment

It is recommended to create a virtual environment for the project:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### Install Dependencies

Install the required packages:

```bash
pip install -r requirements.txt
```

### Install the Package

Install the package locally:

```bash
pip install -e .
```

## Usage

### Example Usage

Here is an example of how to use Data Explorer:

```python
from data_explorer import DataExplorer

file_path = 'examples/example_data.csv'
explorer = DataExplorer()

# Load data
data = explorer.load_data(file_path)
print("Data loaded successfully.")

# Clean data
clean_data = explorer.clean_data(data)
print("Data cleaned successfully.")

# Analyze data
description, correlation = explorer.analyze_data(clean_data)
print("Data analysis completed successfully.")
print("Descriptive Statistics:\n", description)
print("Correlation Matrix:\n", correlation)

# Visualize data
explorer.visualize_data(clean_data)
print("Data visualization completed successfully.")
```

### Running Example Notebooks

You can also explore the functionality using the provided Jupyter notebooks:

1. `examples/example_analysis.ipynb`
2. `examples/example_visualization.ipynb`

Start Jupyter Notebook:

```bash
jupyter notebook
```

Open and run the notebooks to see Data Explorer in action.

## Documentation

For detailed documentation, please refer to the [docs](docs) directory.

- [Index](docs/index.md)
- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Examples](docs/examples.md)

## Running Tests

We use `pytest` for testing. To run the tests, execute:

```bash
pytest
```

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](docs/contributing.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Author

Developed by [Tom Souillard](https://github.com/Tom-Souillard).


<p>&nbsp;</p>
<p>&nbsp;</p>


### Français

# Data Explorer

Data Explorer est un script polyvalent pour l'analyse exploratoire des données, incluant le chargement, le nettoyage, l'analyse descriptive et la visualisation des données. Conçu pour être modulable et réutilisable dans divers projets de science des données.

## Fonctionnalités

- **Chargement des Données** : Charger des données à partir de fichiers CSV.
- **Nettoyage des Données** : Supprimer les doublons et gérer les valeurs manquantes.
- **Analyse Descriptive** : Générer des statistiques descriptives et des matrices de corrélation.
- **Visualisation des Données** : Créer des histogrammes et des cartes thermiques pour la visualisation des données.

## Installation

### Cloner le Dépôt

```bash
git clone https://github.com/Tom-Souillard/data_explorer
cd data_explorer
```

### Créer un Environnement Virtuel

Il est recommandé de créer un environnement virtuel pour le projet :

```bash
python -m venv venv
source venv/bin/activate  # Sous Windows, utilisez `venv\Scripts\activate`
```

### Installer les Dépendances

Installez les packages requis :

```bash
pip install -r requirements.txt
```

### Installer le Package

Installez le package localement :

```bash
pip install -e .
```

## Utilisation

### Exemple d'Utilisation

Voici un exemple d'utilisation de Data Explorer :

```python
from data_explorer import DataExplorer

file_path = 'examples/example_data.csv'
explorer = DataExplorer()

# Charger les données
data = explorer.load_data(file_path)
print("Données chargées avec succès.")

# Nettoyer les données
clean_data = explorer.clean_data(data)
print("Données nettoyées avec succès.")

# Analyser les données
description, correlation = explorer.analyze_data(clean_data)
print("Analyse des données terminée avec succès.")
print("Statistiques Descriptives:\n", description)
print("Matrice de Corrélation:\n", correlation)

# Visualiser les données
explorer.visualize_data(clean_data)
print("Visualisation des données terminée avec succès.")
```

### Exécuter les Notebooks d'Exemple

Vous pouvez également explorer les fonctionnalités en utilisant les notebooks Jupyter fournis :

1. `examples/example_analysis.ipynb`
2. `examples/example_visualization.ipynb`

Lancez Jupyter Notebook :

```bash
jupyter notebook
```

Ouvrez et exécutez les notebooks pour voir Data Explorer en action.

## Documentation

Pour une documentation détaillée, veuillez consulter le répertoire [docs](docs).

- [Index](docs/index.md)
- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Examples](docs/examples.md)

## Exécution des Tests

Nous utilisons `pytest` pour les tests. Pour exécuter les tests, lancez :

```bash
pytest
```

## Contribution

Les contributions sont les bienvenues ! Veuillez lire le fichier [CONTRIBUTING.md](docs/contributing.md) pour les directives sur la manière de contribuer à ce projet.

## Licence

Ce projet est sous licence Apache License 2.0. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Auteur

Développé par [Tom Souillard](https://github.com/Tom-Souillard).
