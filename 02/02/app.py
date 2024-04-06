"""
    Creation de la liste & Affichage des elements de la liste:
        - Definition de liste (Creer la classe)
        - Ajouter methode :
            - ajouter : qui permet d'ajout un element dans la liste
                - Erreur si l'element n'est pas une chaine :
                raise ValueError(...),
                - Element ne doit pas exister dans la liste :
                retourner False
                    et afficher un message (Element existe deja)
            - enlever : permet de supprimer un element de la liste
                - Retourner True si bien enlever sinon False,
            - afficher :
                - Afficher tous les elements de la liste

"""


import logging
import json
import os

from consts import DATA_DIR

log = logging.getLogger()


class BreukhList(list):
    def __init__(self,name="Untitled list"):
        self.name = name
    # Les methode de la clASSE
    def ajouter(self,elmt):
        # if type(elmt) != str:
        if not isinstance(elmt,str):
            raise ValueError("😩 Erreur, on ne prend que des chaine!!!")
        if elmt in self:
            log.error(f"😡 '{elmt}' est deja dans la liste!!!")
            return False
        self.append(elmt)
        return True
    def enlever(self,elmt):
        if elmt in self:
            self.remove(elmt)
            return True
        log.error(f"'{elmt}' n'est pas dans la liste!!!")
        return False
    def afficher(self):
        print(f"Ma liste de '{self.name}' :")
        for element in self:
            print(f"- {element}")
    def sauvegarder(self):
        chemin = os.path.join(DATA_DIR,f"{self.name}.json")
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        with open(chemin,"w") as f:
            json.dump(self,f,indent=4)
        return True

    

l1 =BreukhList('A faire')
# l1.ajouter("8h: Aller a l'ecole")
# l1.ajouter("12h: Faire mes devoirs")
# l1.ajouter("15h: Dormir un peu")
# l1.ajouter("17h: Aller au sport")

l1.ajouter("20h: Aller dormir")
l1.sauvegarder()
