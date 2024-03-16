"""
1) Declarer deux instances de la classe Montre
2) Modifier la marque a partir de classe Montre
3) Modifier la marque de chaque instance

"""

class Montre:
    marque = "Rolex"
    style = "Eguille"
    bracelet = "Cuir"
    prix = 10_000


# 1)
montre_01 = Montre()
montre_02 = Montre()
print(f"Marque de la classe : {Montre.marque}")
print(f"Marque de montre_01 : {montre_01.marque}")
print(f"Marque de montre_02 : {montre_02.marque}")
print("----------------")
# 2)
Montre.marque = "Hublot"
print(f"Marque de la classe : {Montre.marque}")
print(f"Marque de montre_01 : {montre_01.marque}")
print(f"Marque de montre_02 : {montre_02.marque}")
print("----------------")
# 3)
montre_01.marque = "Omega"
montre_02.marque = "TAG Heuer"
print(f"Marque de la classe : {Montre.marque}")
print(f"Marque de montre_01 : {montre_01.marque}")
print(f"Marque de montre_02 : {montre_02.marque}")
print("----------------")