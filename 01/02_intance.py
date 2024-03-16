"""
1) Creer une instance de la classe Montre
2) Afficher l'instance cree
3) Afficher la marque de l'instance
4) Creer une seconde instance de la classe Montre
"""

class Montre:
    marque = "Rolex"
    style = "Eguille"
    bracelet = "Cuir"
    prix = 10_000

# 1)
montre_01 =  Montre()
# 2)
print(montre_01)
# 3)
print(montre_01.marque)
print("----------")
# 4)
montre_02 = Montre()
print(montre_02)
print(montre_02.marque)

