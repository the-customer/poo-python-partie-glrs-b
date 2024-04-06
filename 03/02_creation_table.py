"""
Creation de table (ou tableau):
    - Recuperer le curseur (Permet d'ecrire sur le fichier,
    ou executer les requetes) a partir de l'objet de connexion.
    - Executer une requete avec la methode execute() du curseur:
        Cette methhode permet mettre la requete en memoire
    - Executer le requete dans la base de donnee:
        utilisation de la methode commit() de l'objet de connexion
"""

import sqlite3
# 
conn = sqlite3.connect("./database.db")
# Recuperer le curseur
cursor = conn.cursor()

# Creation de la table:
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS produit(libelle text,prix number,quantite number)
    """
)

# Executer les changements dans la base
conn.commit()

conn.close()