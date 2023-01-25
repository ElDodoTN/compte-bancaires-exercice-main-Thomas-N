#from abc import ABC, abstractmethod
#class Compte(ABC):
    #@abstractmethod
    #def __init__(self,numero_compte,nom_proprietaire,solde_compte):
    #    self.numero_compte = numero_compte
    #    self.nom_proprietaire = nom_proprietaire
    #    self.solde_compte = solde_compte

    #def retrait(self,montant_a_retirer,):
    #    self.montant_a_retirer = montant_a_retirer
    #    montant_retiré = self.solde_compte - self.montant_a_retirer
    #    return f"Vous avez retiré : {montant_a_retirer} $ sur le compte {nom_proprietaire}, Votre solde s'élève maintenant à : {montant_retiré} $"

    #def versement(self,montant_a_verser):
    #    self.montant_a_verser = montant_a_verser
    #    transfer = self.solde_compte + self.montant_a_verser
    #    return f"La valeur de {transfer} à bien été transféré"

    #def afficher_solde(self,solde_compte):
    #    self.solde_compte = solde_compte
    #    account = self.solde_compte
    #    return f"Votre solde actuel est de : {account} $"

    #def __str__(self):
    #    return f"{self.nom_proprietaire,self.numero_compte,self.solde}"

#class CompteCourant(Compte):
    #def negative_balance_limit(self):
    #    pass
    #def appliquer_interets(self): #Ici représente les Agios
    #    montant = self.montant
    #    solde = self.solde
    #    if montant > 0:
    #        solde = montant *(100+2)/100
    #    return solde
    #    pass
    #pass

#class CompteEpargne(Compte):
#    pass

from compte import *
if __name__ == '__main__':
    print('''
__________.__                            __________                __    
\______   \__| ____   __________  __ __  \______   \_____    ____ |  | __
 |     ___/  |/ ___\ /  ___/  _ \|  |  \  |    |  _/\__  \  /    \|  |/ /
 |    |   |  \  \___ \___ (  <_> )  |  /  |    |   \ / __ \|   |  \    < 
 |____|   |__|\___  >____  >____/|____/   |______  /(____  /___|  /__|_ |
        ''')
    nom_proprietaire = input('Entrer votre prénom : ')
    solde = 100
    numero_compte = "eq37fd-x1mp9-eD5wQ"
    print(f"Bienvenue dans la Banque à Picsou {nom_proprietaire},")
    print(f"Votre numéro de compte est : {numero_compte}")
    print(f"Le solde de votre compte est de : {solde} €")
    compte = input("En quoi puis-je vous aider ? \n 1.Accéder au Compte Courant \n 2.Accéder au Compte Eparge \n 3.Quitter la Banque \n")
    if compte == "1":
        print(f"Bienvenue sur votre compte Courant, le solde de votre compte est de {solde} €,que souhaitez-vous faire ?")
        compte_courant = input("1.Faire un dépot \n 2.Faire un retrait \n")
        if compte_courant == "1":
            versement = input(f"Décrivez le montant du versement :")
            #solde += versement
            print(f"Votre solde s'élève à {versement} €")

        if compte_courant == "2":
            retrait = input(f"Décrivez le montant du retrait :")
            #solde -= retrait
            print(f"Votre solde s'élève à {retrait} €")

    if compte == "2":
        print(f"Bienvenue sur votre compte Epargne, le solde est de {solde} €")
        compte_epargne = input("1. Faire un dépot \n2. Faire un retrait \n")
        if compte_epargne == "1":
            versement = input(f"Décrivez le montant du versement : ")
            #solde += versement
            print(f"Votre solde s'élève à {versement} €")
        if compte_epargne == "2":
            retrait = input(f"Décrivez le montant du retrait :")
            #new_solde = solde + retrait
            print(f"Vous avez retiré {retrait} €")
    if compte == "3":
        print("Nous espérons vous revoir bientôt dans la banque à Picsou")
        pass
    #Trouver une solution pour intéragir avec l'interface
    #print(Compte.afficher_solde(Compte,1000))
    #print(Compte.retrait(Compte,999))
