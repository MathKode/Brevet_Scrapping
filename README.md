# Brevet_Scrapping
Un petit code util si on veut créer un tableau .csv de toutes les personnes qui ont eu le brevet dans l'académie de votre choix

# Info
1) Comment fonctionne le code ?

Ce code fonctionne d'une façon très simple : il va rechercher sur le site de l'académie concerné tout les noms des candidats (brut force)

2) Comment faire le brute force ?

Pour cette question, je vous renvois vers un de mes repesitorys "Brute_Force"

3) Comment obtenir les resultats pour un nom ?

Pour ce faire, j'ai du faire un petit travail d'analyse. En effet, après avoir ouvert la console du site (dans network), j'ai remarqué qu'il envoyait toujours la même requête pour obtenir les datas :

Exemple (avec domairon) :
https://cyclades.ac-nancy-metz.fr/publication_A12/publication?filtre=domairon&contexte=eyJjb2RlRG9tYWluZSI6IkROQiIsImNvZGVFbnRpdGVSZXNwb25zYWJsZSI6IkExMiIsImNvZGVTZXNzaW9uIjoiMjAyMTpCOkROQi0yLjMiLCJjb2RlR3JvdXBlRGVjaXNpb24iOiIxIiwiY29kZVF1YWxpZmljYXRpb24iOm51bGwsImNvZGVDb250ZXh0ZVJlZ2xlbWVudGFpcmUiOm51bGwsImNvZGVab25lR2VvZ3JhcGhpcXVlIjpudWxsfQ%3D%3D&_=1625845265472

Exemple (avec cojocaru) :
https://cyclades.ac-nancy-metz.fr/publication_A12/publication?filtre=cojocaru&contexte=eyJjb2RlRG9tYWluZSI6IkROQiIsImNvZGVFbnRpdGVSZXNwb25zYWJsZSI6IkExMiIsImNvZGVTZXNzaW9uIjoiMjAyMTpCOkROQi0yLjMiLCJjb2RlR3JvdXBlRGVjaXNpb24iOiIxIiwiY29kZVF1YWxpZmljYXRpb24iOm51bGwsImNvZGVDb250ZXh0ZVJlZ2xlbWVudGFpcmUiOm51bGwsImNvZGVab25lR2VvZ3JhcGhpcXVlIjpudWxsfQ%3D%3D&_=1625845265472

Vous l'avez peut-être remarqué mais la requête est la même ! Il y a juste l'élément filtre= qui change... Ainsi, on a juste a test tous les urls

Exemple :
filtre=a
filtre=b
filtre=c
...

4) Comment créer un fichier .cvs ?

Pour créer un fichier cvs, c'est vraiment super simple : on écrit ce qu'on veut dans une case puis, pour passer à la case suivante, on met une virgule

Exemple :
Nom,Prénom,Age
Kremer,Mathis,15
Di Martino, Viktoria, 15
Brandenbourger,louise,15
