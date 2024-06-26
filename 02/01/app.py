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

        

    

l1 =BreukhList('Course')
l1.ajouter("Acheter des mangues")
l1.afficher()

l = BreukhList("Liste de personne")




if(l.ajouter("toto")==True):
    print("ajouer ok") 

l.ajouter("titi") 
l.ajouter("tata") 
# l.ajouter(34)
# l.ajouter(["titi"])

l.afficher()

l.enlever("titi")

l.afficher()
