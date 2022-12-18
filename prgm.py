import sys
import os
import unittest
print("hello World")

#exemples d'assert
#assert sum([1, 2, 3]) == 6, "Should be 6"
#assert sum([1, 2, 3]) == 8, "wrong test"

##________________
#print(sys.stdout())
    #assert sys.stdout() == "hello World", "No hello world"
#_____________________

def testVerificationAffichageHelloWorld():
    #verify ID 1
    # etant donne le démarrage du programme,
    # quand je lis la console,
    # alors je vois le texte "hello world"
    print('None')


def testAfficherTauxReduction():
    #verifie ID 12 (depend ID9)
    #etant donne une commande avec un montant de réduction (de 0e),
    #quand j'ai un total et un montant de réduction,
    #alors j'affiche un taux de réduction appliqué à côté du montant de la réduction de la manière suivante, sur une même ligne :
	#       "Discount "+pourcentageReduction +"%"  et tout a droite "-"+montantDeLaReduction
    print('None')


def testInputUserProductName():
    #verifie 18
    #etant donne l'ajout d'un article possédant une quantité et un unit price,
    #quand j'entre la désignation de l'article,
    #alors j'affiche une ligne avec les éléments suivants  :
	#designation + quantity + unit price + articleTotalPrice
    print('None')

def testAfficherMontantTotalReduction():
    #verifie 9 (depend ID4)
    #etant donne un article avec un prix unitaire, une quantité et un prix total par article,
    #quand j'ai une commande avec au moins un article,
    #alors j'affiche un taux de réduction fixe de 0e de la manière suivante :
	#       "Discount " et tout a droite "-"+0e
    print('None')



#id 19
def testReduction20siFR20000():
    # etant donne une commande,
    # quand le montant total HT de la commande est supérieure à 20 000 ET que le code pays est "FR",
    # alors le pourcentage de Réduction (pourcentageReduction) sera de 20%
    print('None')
    
#id 11 (depend ID1)
def afficheTauxReductionDebutProgramme():
    #Etant donné l'ouverture du programme
    #Je veux afficher la liste des taux de réduction au démarrage du programme
    #Afin d'avoir les réductions possibles (en deux colonnes Order value et Discount rate)
    print('None')

# id 2 (depend ID1) parce que afficher prix total sur id 4 c est le total de la liste des articles
def testsaisirPUEtQuantite(prix_unitaire ,quantite):
    #Etant donné une commande
    # Quand j'ajoute un article, je renseigne un prix unitaire et une quantité
    # Alors le prix total de l'article est calculé (articleTotalPrice = quantity*unit price)
    # Et la ligne suivante s'affiche :
    # quantity + unit price + articleTotalPrice

  # Input de la valeur du pu
    #prix_unitaire = float(input("Entrer le prix unitaire: "))
    # Test de la valeur entree
    assert (prix_unitaire > 0), 'Le pu ne peut pas être inferieur ou egale à 0'
    # Input de la quantite
    #quantite = int(input("Entrer la quantite: "))
    # Test du quantite entree
    assert (quantite > 0), 'La quantite ne peut pas être inferieur ou egale à 0'
    # Calcul du prix total
    prix_total = prix_unitaire*quantite
    # Test du prix total
    assert (prix_total == prix_unitaire*quantite), 'La valeur n est pas la bonne, erreur de caclcul'
    # Affichage du prix total
    print(round(prix_unitaire*quantite,3))


 #id 3 (depend ID2)
def testAjoutArticle():
    #etant donné une commande où j'ai terminé de renseigner un article,
    #quand on me propose de rajouter un article et que je réponds oui, 
    #alors je continue l'ajout d'article


    #etant donné une commande où j'ai terminé de renseigner un article,
    #quand on me propose de rajouter un article et que je réponds non, 
    #alors je finis ma commande
    assert (print("nom article 1") != "nom article 1"), 'nom de l article non recupere'

def testDemanderUserSaisieTauxReduction():
    #verifie ID 10 (depend ID9)
    #Etant donne une commande avec un taux de réduction fixe de 0e,
    #quand je renseigne le taux de réduction à appliquer,
    #alors est calculé le total without taxes de la commande et le montant de la réduction,
    #ET on affiche les lignes suivantes :
        #"-----------------------------------------------------"
        #"Total without taxes" + totalHT
        #"Discount " et tout a droite "-"+montant de la réduction+"e"
    print('None')

# id 7 (depend ID6)
def testDemanderCodeEtatEtAfficherTVA(DictionnaireCodeTva,codeEtat):
    #Etant donné la liste des taux de TVA affichées par état,
    #quand je renseigne le code de l'état,
    #alors j'affiche le taux de TVA correspondant de la manière suivante :
        #"Tax" + tauxdeTVA + "%"

    # Code Etat entree
    #codeEtat = input("Veuillez saisir le code Etat: ")
    assert(codeEtat != "" or codeEtat != None),'Erreur code codeEtat'
    assert(DictionnaireCodeTva.get(codeEtat) != None), 'Ce code Etat n existe pas dans la liste'
    # Afficher le tva correspondant si assert passe
    print(DictionnaireCodeTva.get(codeEtat))  

# ID 8 (depend ID7)
def testNePlusAfficherTvaMaisAplLiquer(tva,prix_ht):
    #Etant donné le renseignement du code etat,
    #quand j'affiche le taux de TVA,
    #alors le montant de la TVA est calculé
    #ET j'affiche les élément de la manière suivante :
	#"Tax" + tauxdeTVA + "%" + montant de la TVA
    #ET la liste des taux TVA n'est plus affichée au démarrage de l'application

    # Clearing the Screen
    os.system('cls') # Ca marche pas encore le clear console il reste ca
    assert(tva >= 0), 'Valeur Tva non valide'
    assert(prix_ht >= 0), 'Valeur du prix non valide'
    prix_ttc = prix_ht + ((prix_ht*tva)/100)
    assert(prix_ht + ((prix_ht*tva)/100)), 'Valeur invalide sur le ttc'
    return prix_ttc

# id 14
def testPresaisirTauxReductionA5():
    # Etant donné un montant de commande supérieur à 5000
    # Quand je souhaite appliquer une réduction
    # Alors je présaisis le taux de réduction à 5%
    print('None')

# ID 6
def testListeDesCodesTva(dictionnaireCodeTva):
    assert(dictionnaireCodeTva), 'Il n y a pas de données CodeTva'
    for cle, valeur in CodeTVA.items():
        print("le code pays avec", cle, "vaut : ", valeur) 


# ID 13, 14, 15, 16, 17
# Etant donnees que le prix total HT d'une commande,
# Quand le prix est supérieur à 1000e,
# Alors on attribue un pourcentage de réduction tel que :
# Cas <prix total, pourcentage reduction>
# Cas <1000,3>
# Cas <5000,5>
# Cas <7000,7>
# Cas <10000,10>
# Cas <15000,15>
def testVerificationPresaisiTauxReduct(prix_total,pourcentage_reduction):
    # Notre reduction dependra du prix total
    # prix total pour la 13
    if(prix_total >= 1000 and prix_total < 5000):
        assert pourcentage_reduction == 3, 'Le pourcentage de reduction ne correspond pas au prix total'
        pourcentage_reduction = 3
    # Pour la 14
    elif(prix_total >= 5000 and prix_total < 7000):
        assert pourcentage_reduction == 5, 'Le pourcentage de reduction ne correspond pas au prix total'
        pourcentage_reduction = 5
    # Pour la 15
    elif(prix_total >= 7000 and prix_total < 10000):
        assert pourcentage_reduction == 7, 'Le pourcentage de reduction ne correspond pas au prix total'
        pourcentage_reduction = 7
    # Pour la 16
    elif(prix_total >= 10000 and prix_total < 15000):
        assert pourcentage_reduction == 10, 'Le pourcentage de reduction ne correspond pas au prix total'
        pourcentage_reduction = 10
    # Pour la 17
    elif(prix_total >= 15000):
        assert pourcentage_reduction == 15, 'Le pourcentage de reduction ne correspond pas au prix total'
        pourcentage_reduction = 15
    else:
        assert False, 'Pas de reduction sur la tarif de base avec la valeur du prix total {}'.format(prix_total)
    return pourcentage_reduction

# id 4 (depend ID2)
def testAfficherLePrixTotal():
    # Etant donné une commande possédant au moins 1 article,
    # quand je veux compléter ma commande
    # alors j'affiche une ligne de la manière suivante :
     #"-----------------------------------------------------"
        #"Total without taxes" + totalHT
    print('none')

#ID 5 (depend ID2)
def testCalculPrixTTC():
    # etant donné les articles saisis
    # quand je veux compléter ma commande
    # alors on calcule le prix TTc (prixTTC = montant hors taxe - réduction + montant TVA) et l'affiche de la maniere suivante
        #"-----------------------------------------------------"
        #"Total prices" + total TTC
    print('None')
    



# Les codes TVA
CodeTVA = {'FR': 20, 'BE': 12,'GB': 10,'CA': 11,'BA': 0.5}










##DEBUT DU PROGRAMME

nomArticle = input("Ajoutez le nom de l'article : ")
print("nom de l'article: " + nomArticle)

##SUITE DE TESTS AUTOMATISES

#testVerificationAffichageHelloWorld()
testAjoutArticle()







########################################################################

def testReductionDe7pourcent():
    #verifie ID 15
    # etant donne une commande,
    # quand le montant total de la commande supérieure à 7000e,
    # alors le pourcentage de Réduction (pourcentageReduction) sera de 7%
    print('None')

#ID 13
def testPresaisirTaux3():
    #etant donné mon prix total
    #quand mon total est au dessus de 1000
    #alors je presaisi mon taux a 3%
    print('None')