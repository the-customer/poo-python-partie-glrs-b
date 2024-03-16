"""
l'affichage d'un objet est tres bizarre et c'est explicite.
Pour pouvoir afficher un objet et avoir les donnees souhaitees alors il
faut implenter la methode __str__
"""
class Montre:
    nbre = 0
    def __init__(self,marque,style,bracelet,prix) -> None:
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        self.prix = prix
        Montre.nbre += 1
    
    # Methode Statique
    @staticmethod
    def afficher_heure() -> str:
        from datetime import datetime
        date = datetime.now()
        return "Il est : {}".format(date.strftime("%H:%M:%S"))
    # Methode de classe
    @classmethod
    def Rolex(cls):
        return cls("Rolex","Aiguille","Cuir",25_000)

    @classmethod
    def Casio(cls):
        return cls("Casio","Electronique","Metal",15_000)
    @classmethod
    def nbre_montre_1(cls):
        print(f"Le nombre de montre est {cls.nbre}")
    @staticmethod
    def nbre_montre_2():
        print(f"Le nombre de montre est {Montre.nbre}")
    
    def __str__(self) -> str:
        return f"<Montre : {self.marque} - {self.bracelet} - {self.prix} >"

rolex01 = Montre.Rolex()
rolex02 = Montre.Rolex()
autre = Montre("Autre Marque","Electonique","Matalique",10000)
casio01 = Montre.Casio()


print(casio01)
