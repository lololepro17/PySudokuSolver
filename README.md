# Sudoku Solver

**Description** : Ce projet est une application Python permettant de résoudre des grilles de sudoku. Il est divisé en plusieurs modules pour faciliter l’organisation, l’extension et la maintenance du code. Chaque module est géré dans une branche dédiée, afin de séparer les différentes fonctionnalités et étapes de développement.

## Fonctionnalités Principales
1. **Lecture et validation des données d'entrée** : Chargement de la grille de sudoku depuis un fichier ou via une entrée utilisateur, avec vérification de la validité des données.
2. **Affichage et interface utilisateur** : Affichage de la grille de sudoku et des étapes de la résolution, soit dans le terminal, soit dans une interface graphique.
3. **Résolution automatique** : Utilisation d'un algorithme pour résoudre automatiquement la grille de sudoku.
4. **Tests et validation** : Tests unitaires pour vérifier la fiabilité et la performance du programme.

## Structure des Branches

| Branche               | Description                                                                                  |
|-----------------------|----------------------------------------------------------------------------------------------|
| `main`                | Branche principale contenant la version stable du projet et intégrant toutes les fonctionnalités. |
| `lecture-validation`  | Contient les fonctions de chargement et de validation des grilles de sudoku.                  |
| `affichage-interface` | Gère l'affichage de la grille et les options de l’interface utilisateur.                      |
| `resolution-algorithm` | Implémente l’algorithme de résolution automatique de sudoku.                                |
| `tests-validation`    | Contient les tests unitaires pour valider le fonctionnement et la performance du programme.   |
| `documentation`       | Branche dédiée à la documentation, contenant des guides, glossaires, et des exemples d’utilisation. |

## Installation

1. Clonez le dépôt sur votre machine :

```bash
   git clone https://github.com/ton_nom_utilisateur/SudokuSolver.git
   cd SudokuSolver
```

2. Installez les dépendances requises :

```bash
pip install -r requirements.txt
```
*(Note:Il faudrat ajouter les package utiliser au fur à mesure.)*

## Utilisation 

- CChaque module peut être testé séparément en changeant de branche :

```bash
git checkout nom_de_la_branche
```

- Suivez les instructions de chaque branche pour tester ou développer des fonctionnalités spécifiques.