import sys
import unittest
print("hello World")

#exemples d'assert
#assert sum([1, 2, 3]) == 6, "Should be 6"
#assert sum([1, 2, 3]) == 8, "wrong test"


def testVerificationAffichageHelloWorld():
    #verify ID 1
    # etant donne le démarrage du programme,
    # quand je lis la console,
    # alors je vois le texte "hello world"
    
    #print(sys.stdout())
    #assert sys.stdout() == "hello World", "No hello world"
    print('None')


def testAfficherTauxReduction():
    #verifie ID 12
    #etant donne une commande
    #quand je demande le montant
    #alors on m'affiche le taux de reduction appliqué a coté
    print('None')

def testAfficheReductionDe7pourcent():
    #verifie ID 15
    # etant donne une commande ,
    # quand celle ci est supérieure à 7000e,
    # alors je veux pouvoir présaisir le taux à 7%
    print('None')

def testInputUserProductName():
    #verifie 18
    #etant donné une commande
    #quand je choisis mon article
    #alors on m'affiche la designation 
    print('None')

def testAfficherMontantTotalReduction():
    #verifie 9
    #etant donné une commande,
    #quand je veux visualiser la commande
    #alors je vois le montant 0 comme réduction fixe
    print('None')

# id 2
def testSaisirPUEtQuantite():
    # Etant donné une commande
    # Quand je demande un prix unitaire et une quantité
    # Alors je calcule et j'imprime un prix total
    print('None')

#id 19
def testReduction20siFR20000():
    #Etant donné une commande
    #Je veux une réduction de 20% si le code pays est FR et le prix total HT > 20 000
    #Afin d'avoir le prix total à payer après réduction
    print('None')
    
#id 11
def afficheTauxReductionDebutProgramme():
    #Etant donné l'ouverture du programme
    #Je veux afficher la liste des taux de réduction au démarrage du programme
    #Afin d'avoir les réductions possibles
    print('None')

# id 4
def testAfficherPrixTotal():
    # Etant donné ma saisie
    # Quand j'ai terminé ma commande
    # Alors j'affiche le prix total
    print('None')


 #id 3
def testAjoutArticle():
    #etant donné une commande
    #quand je veux completer mon panier 
    #alors j'ajoute des articles
    assert (print("nom article 1") != "nom article 1"), 'nom de l article non recupere'

def testDemanderUserSaisieTauxReduction():
    #verifie ID 10
    #etant donne une commande,
    #
    print('None')

# id 7
def testDemanderCodeEtatEtAfficherTVA():
    # Etant donné une saisie
    # Quand je souhaite calculer le prix TTC
    # Alors je demande le code de l'état et j'affiche le code TVA correspondant
    print('None')

# id 8
def testNePlusAfficherTVAMaisAppliquerAuCalcul():
    # Etant donné une saisie
    # Quand je souhaite plus afficher le code TVA
    # Alors je l'applique au calcul
    print('None')

# id 14
def testPresaisirTauxReductionA5():
    # Etant donné un montant de commande supérieur à 5000
    # Quand je souhaite appliquer une réduction
    # Alors je présaisis le taux de réduction à 5%
    print('None')

#id 6
def testListeDesCodesTva():
    #etant donné l'ouverture du programme
    #quand je veux utiliser le programme
    #alors on m'affiche le code TVA
    print('None')

#ID 5
def calculPrixTTC():
    print('None')
    

#ID 13
def testPresaisirTaux3():
    #etant donné mon prix total
    #quand mon total est au dessus de 1000
    #alors je presaisi mon taux a 3%
    print('None')










##DEBUT DU PROGRAMME

nomArticle = input("Ajoutez le nom de l'article : ")
print("nom de l'article: " + nomArticle)

##SUITE DE TESTS AUTOMATISES

#testVerificationAffichageHelloWorld()
testAjoutArticle()