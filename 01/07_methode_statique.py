"""
1) Creer une methode qui permet d'afficher 
les details sur le nombre de creer

SOLUTION:
on peut le faire avec une methode de classe 
ou  bien avec une methode statique : avec le decorateur @staticmethod:
les methodes statique ne prennent en argument ni le SELF ni CLS, et qu'on
peut les appeler avec un objet ou avec la classe.
exemple:
Changer la methode qui afficher l'Heure en une methode statique
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

rolex01 = Montre.Rolex()
rolex02 = Montre.Rolex()
autre = Montre("Autre Marque","Electonique","Matalique",10000)
casio01 = Montre.Casio()

# Montre.nbre_montre_1()
Montre.nbre_montre_2()
casio01.nbre_montre_2()

print(Montre.afficher_heure())
print(casio01.afficher_heure())