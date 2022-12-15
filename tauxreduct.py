# Etant donnees qu'une commande total a la somme de X euros
# Alors une valeur placeholder
# Cas <prix total, pourcentage reduction>
# Cas <1000,3>
# Cas <5000,5>
# Cas <7000,7>
# Cas <10000,10>
# Cas <15000,15>
# ID 13, 14, 15, 16,17
def testVerificationPresaisiTauxReduct(prix_total,pourcentage_reduction):
    # Notre reduction dependra du prix total
    # prix total pour la 13
    if(prix_total >= 1000 and prix_total < 5000):
        assert pourcentage_reduction == 3, 'Le pourcentage de reduction ne correspond pas au prix total'
    # Pour la 14
    elif(prix_total > 1000 and prix_total <= 5000):
        assert pourcentage_reduction == (prix_total % 1000), 'Le pourcentage de reduction ne correspond pas au prix total'
    else:
        assert False, 'Pas de reduction sur la tarif de base avec la valeur du prix total {}'.format(prix_total)