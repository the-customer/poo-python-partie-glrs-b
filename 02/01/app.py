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
        return False
    



l = BreukhList("Liste de personne")




l.ajouter("toto") 
l.ajouter("toto") 
l.ajouter(34)
l.ajouter(["titi"])

print(l)
