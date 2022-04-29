# Base_article_scientifique

## Contexte du projet

Le centre de recherche Breizhmeiz International souhaite un petit module d'accès simple aux publications scientifiques. On vous demande de mettre en place une base de données MongoDB, orientée documents, pour gérer l'accès à ces publications. De votre coté, vous allez tester les datas grâce à un petit script Python.

## Mise en place de la base de données

Dans le cadre de ce projet nous utilisons un conteneur **docker** pour déployer la base de données *mongoDB*.
Une fois le conteneur démarré :
1. Copier le fichier *dblp.json* dans le conteneur : ```sudo docker cp dblp.json mongodb:./dblp.json```  
2. Création de la base de donnée à partir du fichier *json* : `sudo docker exec -it mongodb mongoimport --db=DBLP --collection=publis --file=dblp.json -u=root --authenticationDatabase=admin -p=`

## Manipulation de la base de données

La classe python __*DataAccess*__ permet de manipuler la base de donnée mongo, pour l'utiliser il suffit de l'importer :   
`from DataAccess import *`

Les méthodes de classe qui la compose :
- `connexion()` : permet d'établir la connexion avec la base de donnée.
- `deconnexion()` : permet de fermer la connexion à la base de données
- `nb_document(condition={})` : permet de compter le nombre de document selon une condition. Par défaut condition est un dictionnaire vide, permétant de récupérer le nombre total de document.
- `lister_document(condition={}, trie=None)` : permet de lister tous les documents selon une condition, ainsi que de les triers selon un champ. Par défaut condition est un dictionnaire vide, et trie vaut *None*.
- `unique(condition)` : permet de récupérer les valeurs unique présent dans un champs.
- `charger_fichier()` : permet de d'ajouter en base, des documents présents dans un fichier *json*. Le fichier est sélectionnable grâce à une fenêtre pop-up.  
__*Attention*__ *: Si des documents du fichier sont déjà présent en base, la fonction s'arrêtera avec une erreur.*

## Tâches du projet

Les tâches à faire pour ce projet ont été réalisé dans le fichier *commandes.py*.

- [x] Compter le nombre de documents de la collection publis
- [x] Lister tous les livres (type “Book”)
- [x] Lister les livres depuis 2014
- [x] Lister les publications de l’auteur “Toru Ishida”
- [x] Lister tous les auteurs distincts
- [x] Trier les publications de “Toru Ishida” par titre de livre
- [x] Compter le nombre de ses publications
- [x] Compter le nombre de publications depuis 2011 et par type
- [x] Compter le nombre de publications par auteur et trier le résultat par ordre croissant  
  
**Bonnus :** 
- [x] demande le chemin d'un fichier json, insére un ou plusieurs nouveaux documents, à partir de ce fichier, dans la collection publis
