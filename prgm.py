
def init():
    print("Hello World")

def saisirPUEtQuantite(quantite, prixUnitaire):
    return ("" + str(quantite) + "     " + str(prixUnitaire) + "     " + str(int(quantite)*int(prixUnitaire)))

if __name__ == "__main__":
    init()

    quantite=input("Combien voulez vous d'article?")
    prixU=input("Quel est le prix unitaire de l'article?")
    print(saisirPUEtQuantite(quantite,prixU))


