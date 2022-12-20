commande = {}
ajouterArticle=""

def init():
    print("Hello World")
    

def saisirPUEtQuantite(quantite, prixUnitaire):
    return ("" + str(quantite) + "     " + str(prixUnitaire) + "     " + str(int(quantite)*int(prixUnitaire)))

def creerUnArticle(quantite, prixU):
    if quantite == None :
        quantite=input("Combien voulez vous d'article?")
    if prixU == None :
        prixU=input("Quel est le prix unitaire de l'article?")
    commande[len(commande)] = [int(quantite), int(prixU)]
    return(saisirPUEtQuantite(quantite,prixU))

def proposerAjouterArticle():
    choix=input("Voulez vous ajouter un article? o pour oui, n pour non ")
    ajouterUnArticle(choix)

def printCommandeEntier():
    for article in commande:
        print(saisirPUEtQuantite(commande[article][0],commande[article][1]))

def ajouterUnArticle(choix):
    if choix =='o':
        print(creerUnArticle(None, None))
    if choix =='n':
        printCommandeEntier()
    else:
        proposerAjouterArticle()

if __name__ == "__main__":
    init()
    print(creerUnArticle(None, None))
    proposerAjouterArticle()
    

