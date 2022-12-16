import sys
import os
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

# id 2 parce que afficher prix total sur id 4 c est le total de la liste des articles
def testsaisirPUEtQuantite(prix_unitaire ,quantite):
    # Etant donné ma saisie
    # Quand j'ai terminé ma commande
    # Alors j'affiche le prix total
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
def testDemanderCodeEtatEtAfficherTVA(DictionnaireCodeTva,codeEtat):
    # Code Etat entree
    #codeEtat = input("Veuillez saisir le code Etat: ")
    assert(codeEtat != "" or codeEtat != None),'Erreur code codeEtat'
    assert(DictionnaireCodeTva.get(codeEtat) != None), 'Ce code Etat n existe pas dans la liste'
    # Afficher le tva correspondant si assert passe
    print(DictionnaireCodeTva.get(codeEtat))  

# ID 8
def testNePlusAfficherTvaMaisAplLiquer(tva,prix_ht):
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


    
# Etant donnees qu'une commande total a la somme de X euros
# Alors une valeur placeholder
# Cas <prix total, pourcentage reduction>
# Cas <1000,3>
# Cas <5000,5>
# Cas <7000,7>
# Cas <10000,10>
# Cas <15000,15>
# ID 13, 14, 15, 16,17
# Le Test
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

# id 4
def testAfficherLePrixTotal():
    # Etant donné les articles saisis
    # quand je veux compléter ma commande
    # alors j'affiche le prix total
    print('none')

#ID 5
def testCalculPrixTTC():
    # etant donné les articles saisis
    # quand on demande le pourcentage de TVA
    # alors on calcule le prix TTc
    print('None')
    

#ID 13
def testPresaisirTaux3():
    #etant donné mon prix total
    #quand mon total est au dessus de 1000
    #alors je presaisi mon taux a 3%
    print('None')

# Les codes TVA
CodeTVA = {'FR': 20, 'BE': 12,'GB': 10,'CA': 11,'BA': 0.5}










##DEBUT DU PROGRAMME

nomArticle = input("Ajoutez le nom de l'article : ")
print("nom de l'article: " + nomArticle)

##SUITE DE TESTS AUTOMATISES

#testVerificationAffichageHelloWorld()
testAjoutArticle()