#Q1
class CompteBancaire:

    def __init__(self, nom, sommeInitiale):

        self.nom = nom
        self.sommeInitiale = sommeInitiale


    def crediter(self, sommeAjouter):

        self.sommeInitiale += sommeAjouter



    def debiter(self, sommeAReduire):

        self.sommeInitiale -= sommeAReduire
        

    def __repr__(self):

        return f"Le compte de M./Mme. {self.nom} est de {self.sommeInitiale} €"


#Q2
"""
compte=CompteBancaire("dupond",100)
compte.crediter(10)
print(compte)
print(compte.debiter(20))
print(compte)
"""
#Q3
"""
comptes=[]
comptes.append(CompteBancaire("Stark",1000))
comptes.append(CompteBancaire("Banner",500))
comptes.append(CompteBancaire("Parker",700))
comptes.append(CompteBancaire("Rogers",600))
comptes.append(CompteBancaire("Wayne",1500))
comptes.append(CompteBancaire("Prince",2500))

def printAccounts(comptes):
    for i in range(len(comptes)):
        print(comptes[i])
"""
#Q4
"""
comptes=[]
comptes.append(CompteBancaire("Stark",1000))
comptes.append(CompteBancaire("Banner",500))
comptes.append(CompteBancaire("Parker",700))
comptes.append(CompteBancaire("Rogers",600))
comptes.append(CompteBancaire("Wayne",1500))
comptes.append(CompteBancaire("Prince",2500))

def printAccounts(comptes):
    for i in range(len(comptes)):
        print(comptes[i])

def debiteXArgent(argent_a_debiter, comptes):

    for i in range(len(comptes)):
        comptes[i].debiter(argent_a_debiter)
printAccounts(comptes)
print("<<----------------------->>")
debiteXArgent(20, comptes)
printAccounts(comptes)
"""