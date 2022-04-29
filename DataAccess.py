from pymongo import MongoClient
import json
import tkinter as tk
from tkinter import filedialog
from tqdm import tqdm

class DataAccess:

    usr = "root"
    pwd = "pass12345"
    host = "localhost"
    port = 27017
    db_name = "DBLP"
    collection_name = "publis"

    @classmethod
    def connexion(cls):
        # connexion à mongo
        cls.client = MongoClient(
            host=cls.host,
            port=cls.port,
            username=cls.usr,
            password=cls.pwd
        )

        # selectionné la bdd
        cls.db = cls.client[cls.db_name]

        # selectionné la collection
        cls.collection = cls.db[cls.collection_name]

    @classmethod
    def deconnexion(cls):
        cls.client.close()

    @classmethod
    def nb_document(cls, condition={}):
        return cls.collection.count_documents(condition)

    @classmethod
    def lister_document(cls, condition={}, trie=None):
        return list(cls.collection.find(condition, sort=trie))
    
    @classmethod
    def unique(cls, condition):
        return cls.collection.distinct(condition)

    @classmethod
    def charger_fichier(cls):
        tk.Tk().withdraw()
        filename = filedialog.askopenfilename()
        print(filename)
        
        lst_article = []
        with open(filename, 'r') as f:
            for objetJSON in tqdm(f):
                lst_article.append(json.loads(objetJSON))
        
        cls.collection.insert_many(lst_article)
        