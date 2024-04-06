"""
on va utiliser la base de donnee SQLITE.
c'est une base de donnees (un module) qui est installé
par defaut.
"""
# 1. Importation:
import sqlite3

# 2. Creer la connexion :
# si le fichier de la base de donees n'existe pas
# alors il le crée sinon il le met a jour
conn = sqlite3.connect("./database.db")

# 3. Fermer la connexion avec la base de de donnees.
conn.close()
