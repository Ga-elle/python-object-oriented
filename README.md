# python-object-oriented
OPENCLASSROOM Découvrez la programmation orientée objet avec Python


# Apprenez la Programmation Orientée Objet avec Python

Projet servant de fil rouge au cours "Apprenez la POO avec Python", disponible sur OpenClassrooms.
Correction disponible https://github.com/OpenClassrooms-Student-Center/la_poo_avec_python

Nous simulons ici un monde virtuel peuplé de 100 000 personnes. Nous cherchons à connaître :

- à partir de quelle densité de population les personnes sont moins agréables que la moyenne,
- à partir de quel âge les personnes gagnent plus d'argent que la moyenne.
Lorsque le programme se lance, une première fenêtre affiche un graphique concernant la densité de population puis une seconde concernant le revenu.

## Installation de dépendences
Pour tracer des graphes, vous allez avoir besoin d'installer matplotlib :

```
pip install matplotlib
```

## Données
100 000 agents ont été créés grâce à PPLAPI.

Si vous souhaitez en générer de nouveaux, entrez la commande suivante :

```
./download_agents -d agents-100k.json -c 100000
```

## Execution du programme

Lancer le programme
```
./model.py agents-100k.json
```
