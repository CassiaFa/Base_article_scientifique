# Créer la base DBLP
# ajouter une collection publis
# importer dans la base les données du fichier dblp.json (Ca peut prendre un peu de temps)
# écrire le script Python pour tester la base, exécuter le script et vérifier les résultats.

from DataAccess import *
from pprint import pprint

DataAccess.connexion()
# Le script Python doit permettre de : 
# Compter le nombre de documents de la collection publis; X
DataAccess.nb_document()
# Lister tous les livres (type “Book”) ; X
condition = {"type" : "Book"}
lst_livres = DataAccess.lister_document(condition)
pprint(lst_livres)

# Lister les livres depuis 2014 ; X

condition = {
    "type" : "Book",
    "year" : {"$gte" : 2014}
}
lst_livres = DataAccess.lister_document(condition)
pprint(lst_livres)

# Lister les publications de l’auteur “Toru Ishida” ; X

condition = {
    "authors" : {"$in": ["Toru Ishida"]}
}
lst_livres = DataAccess.lister_document(condition)
pprint(lst_livres)

# Lister tous les auteurs distincts ; X

lst_auteur = DataAccess.unique("authors")
print(lst_auteur)

# Trier les publications de “Toru Ishida” par titre de livre ; 

condition = {
    "authors" : {"$in": ["Toru Ishida"]}
}

trie = [("title", 1)] # pymongo.Ascending = 1 pymongo.DESCENDING = -1

lst_livres = DataAccess.lister_document(condition, trie)
pprint(lst_livres)

# Compter le nombre de ses publications ; 

print(f"Nombre de document trouvé : {len()}")

# Compter le nombre de publications depuis 2011 et par type ;

type_documents = DataAccess.unique("type")

for t in type_documents:
    condition = {
        "type" : t,
        "year" : {"$gte" : 2011}
    }

    nb_documents = {
        t : DataAccess.nb_document(condition)
    }

    print(f"Il y a {nb_documents[t]} {t}\n")

# Compter le nombre de publications par auteur et trier le résultat par ordre croissant ;

nb_publi_auteur = DataAccess.collection.aggregate([{"$unwind" : "$authors"}, {"$sortByCount" : "$authors"} ])

for i in nb_publi_auteur:
    print(i)


# nb_publi_auteur = {}

# for a in lst_auteur:
#     condition = {"authors" : a}

#     nb_publi_auteur = {a : DataAccess.nb_document(condition)}

# nb_publi_auteur = {k: v for k, v in sorted(nb_publi_auteur.items(), key=lambda item: item[1])}




# Tous les affichages se font dans la console.

# Et s'il vous reste du temps écrire un petit script qui : demande le chemin d'un fichier json, insére un ou plusieurs nouveaux documents, à partir de ce fichier, dans la collection publis.

# Pour tester ce dernier script, créer un fichier json à partir des informations trouvées sur le site proposé en lien.

DataAccess.connexion()