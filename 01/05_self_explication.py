"""
1) Ajouter une methode a la classe Montre (afficher l'heure) : 
sans le mot clef SELF
2) Creer un objet et appeler la methode afficher
"""

class Montre:
    def __init__(self,marque,style,bracelet,prix) -> None:
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        self.prix = prix
    
    def afficher_heure(self):
        return "Il est : 11:30"
    
montre_01 = Montre("TAG Heuer","Eletronique","Metal",25_000)

print(montre_01.afficher_heure())

# print(Montre.afficher_heure(montre_01))