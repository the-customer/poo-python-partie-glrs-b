"""
1) Creer la methode __init__:
    C'est le constructeur qui est appelé a chaque qu'on
    cree un objet (instance)
"""
class Montre:
    # Attribut de classe
    nbre_montre = 0
    def __init__(self,marque,style,bracelet,prix) -> None:
        # Attributs d'objet
        self.marque = marque
        self.style = style
        self.bracelet = bracelet
        self.prix = prix
        Montre.nbre_montre += 1



montre_01 = Montre("TAG Heuer","Eletronique","Metal",25_000)
montre_02 = Montre("OMEGA","Eletronique","OR",2_050_000)
montre_03 = Montre("OMEGA","Eletronique","OR",2_050_000)


# print(Montre.marque) # ❌
print(montre_01.marque) # ✅
print("Marque : {}".format(montre_01.marque))
print(Montre.nbre_montre)
# print(montre_01.nbre_montre) # 😡 Pas recommander



# m = input("Entrer la marque : ")
# s = input("Entrer le style : ")
# b = input("Entrer le type de bracelet : ")
# p = int(input("Entrer le prix: "))
# montre_03 = Montre(m,s,b,p)
# montre_04 = Montre(
#                     input("Entrer la marque : "),
#                     input("Entrer le style : "),
#                     input("Entrer le type de bracelet : "),
#                     int(input("Entrer le prix: ")))
# print(montre_03.marque)