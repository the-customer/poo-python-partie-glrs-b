"""
On suppose que 90% des montres vendues par la boutique sont  des :
    - Rolex à aiguille en cuir
    - Casio Electronique en Metal
Proposer une methode rapide pour creer ces montres
SOLUTION:
    Creer des methodes de class avec le decorateur : @classmethod
"""

class Montre:
    nbre = 0
    def __init__(self,marque,style,bracelet,prix) -> None:
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        self.prix = prix
        Montre.nbre += 1
    
    # Methode d'instance
    def afficher_heure(self) -> str:
        return "Il est : 11:30"
    # Methode de classe
    @classmethod
    def Rolex(cls):
        return cls("Rolex","Aiguille","Cuir",25_000)

    @classmethod
    def Casio(cls):
        return cls("Casio","Electronique","Metal",15_000)
    
    
rolex01 = Montre.Rolex()
rolex02 = Montre.Rolex()
autre = Montre("Autre Marque","Electonique","Matalique",10000)
casio01 = Montre.Casio()

