### English

# Data Explorer 

Data Explorer is a versatile script for exploratory data analysis, including data loading, cleaning, descriptive analysis, and visualization. Designed to be modular and reusable in various data science projects.

## Features

- **Data Loading**: Load data from CSV files.
- **Data Cleaning**: Remove duplicates and handle missing values.
- **Descriptive Analysis**: Generate descriptive statistics and correlation matrices.
- **Data Visualization**: Create histograms and heatmaps for data visualization.

## Installation

Clone the repository and install the required packages:

```bash
git clone https://github.com/Tom-Souillard/data-explorer.git
cd data-explorer
pip install -r requirements.txt
```

## Usage

Example usage of Data Explorer:

```python
from data_explorer import DataExplorer

file_path = 'examples/example_data.csv'
explorer = DataExplorer()
data = explorer.load_data(file_path)
clean_data = explorer.clean_data(data)
description, correlation = explorer.analyze_data(clean_data)
explorer.visualize_data(clean_data)
```

For more detailed examples, check the [examples](examples) directory.

## Documentation

For detailed documentation, please refer to the [docs](docs) directory.

- [Index](docs/index.md)
- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Examples](docs/examples.md)

## Contributing

Contributions are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the APACH License. See the [LICENSE](LICENSE) file for details.
___

<p>&nbsp;</p>
<p>&nbsp;</p>


### Francais

# Data Explorer

Data Explorer est un script polyvalent pour l'analyse exploratoire des données, incluant le chargement, le nettoyage, l'analyse descriptive et la visualisation des données. Conçu pour être modulable et réutilisable dans divers projets de science des données.

## Fonctionnalités

- **Chargement des Données**: Charger des données à partir de fichiers CSV.
- **Nettoyage des Données**: Supprimer les doublons et gérer les valeurs manquantes.
- **Analyse Descriptive**: Générer des statistiques descriptives et des matrices de corrélation.
- **Visualisation des Données**: Créer des histogrammes et des cartes thermiques pour la visualisation des données.

## Installation

Clonez le repository et installez les packages requis :

```bash
git clone https://github.com/Tom-Souillard/data-explorer.git
cd data-explorer
pip install -r requirements.txt
```

## Utilisation

Exemple d'utilisation de Data Explorer :

```python
from data_explorer import DataExplorer

file_path = 'examples/example_data.csv'
explorer = DataExplorer()
data = explorer.load_data(file_path)
clean_data = explorer.clean_data(data)
description, correlation = explorer.analyze_data(clean_data)
explorer.visualize_data(clean_data)
```

Pour des exemples plus détaillés, consultez le répertoire [examples](examples).

## Documentation

Pour une documentation détaillée, veuillez consulter le répertoire [docs](docs).

- [Index](docs/index.md)
- [Installation](docs/installation.md)
- [Usage](docs/usage.md)
- [Examples](docs/examples.md)

## Contribution

Les contributions sont les bienvenues ! Pour les changements majeurs, veuillez d'abord ouvrir un ticket pour discuter de ce que vous souhaitez changer.

## Licence

Ce projet est sous licence Apache Voir le fichier [LICENSE](LICENSE) pour plus de détails.