# Data Analyzer - Projet Python avec Copilot

Un outil Python d'analyse de données CSV, développé avec l'aide de GitHub Copilot. Il effectue des analyses statistiques, produit des visualisations, et propose une interface en ligne de commande.

## Installation

```bash
cd data-analyzer
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sous Windows
pip install -r requirements.txt  # ou installe manuellement : pandas matplotlib seaborn pytest
```

## Structure du projet

```
data-analyzer/
├── data/               # Fichiers CSV
├── src/                # Modules principaux
├── tests/              # Tests unitaires
├── results/            # Visualisations générées
├── main.py             # Interface ligne de commande
└── README.md
```

## Utilisation

```bash
python main.py data/sample_data.csv --analysis summary
```

Options :

- `--analysis` : `summary`, `time`, `top`
- `--plot` : `bar`, `line`, `pie`, `heatmap`
- `--output` : chemin du fichier image à sauvegarder (ex: `results/plot.png`)

## Exemple

```bash
python main.py data/sample_data.csv --analysis time --plot line --output results/time_plot.png
python main.py data/sample_data.csv --analysis top --plot bar --output results/top_categories.png
```

## Lancer les tests

```bash
pytest tests/
```

## Fonctionnalités

- Chargement de données CSV
- Statistiques par catégorie
- Tendances de dépenses dans le temps
- Segmentation client
- Visualisation avec matplotlib/seaborn

## Bonus possibles

- Export JSON/Excel
- Interface web avec Streamlit
- Visualisation interactive avec Plotly

---

Projet réalisé par Cabrel DHOSSOU – propulsé par GitHub Copilot
