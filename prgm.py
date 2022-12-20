commande = {}
ajouterArticle=""

def init():
    print("Hello World")
    

def saisirPUEtQuantite(quantite, prixUnitaire, designation):
    return (designation + "     " + str(quantite) + "     " + str(prixUnitaire) + "     " + str(int(quantite)*int(prixUnitaire)))

def creerUnArticle(quantite, prixU, designation):
    if quantite == None :
        quantite=verifyInput('int',"Combien voulez vous d'article?", "quantité est un nombre")
    if prixU == None :
        prixU=verifyInput('int',"Quel est le prix unitaire de l'article?", "prix unitairte non correct")
    if designation == None :
        designation=input("Quel est la designation de l'article?")
    commande[len(commande)] = [int(quantite), int(prixU), designation]
    return(saisirPUEtQuantite(quantite,prixU,designation))

# verification de l'input et retourne la valeur quand c est un integer entre en l input
def verifyInput(type_var, message, messageErreur, variable=None):
    # Si on veut que ce soit un integer
    if type_var == 'int':
        while isinstance(variable, str) or (variable == None):
            try:
                x = int(input(message))
                return x
                break
            except ValueError:
                print(messageErreur)

def proposerAjouterArticle():
    choix=input("Voulez vous ajouter un article? o pour oui, n pour non ")
    ajouterUnArticle(choix)

def printCommandeEntier():
    for article in commande:
        print(saisirPUEtQuantite(commande[article][0],commande[article][1],commande[article][2]))

def ajouterUnArticle(choix):
    if choix =='o':
        print(creerUnArticle(None, None, None))
    if choix =='n':
        printCommandeEntier()
    else:
        proposerAjouterArticle()

def calculerTotalHTCommande():
    totalHT=0
    for article in commande:
        totalHT = int(commande[article][0])*int(commande[article][1]) + totalHT
    return totalHT

def printFooter():
    print("-------------------------------")
    print("Total without taxes" + "     " + str(calculerTotalHTCommande()))
    print(ligneDeReduction(0))
    print("-------------------------------")



def ligneDeReduction(montantTotal):
    return "Discount               -"+str(0)

if __name__ == "__main__":
    init()
    print(creerUnArticle(None, None, None))
    proposerAjouterArticle()
    printFooter()
