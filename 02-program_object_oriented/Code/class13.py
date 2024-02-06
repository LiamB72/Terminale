import datetime

date = datetime.datetime.now()
annee = date.year


class Employe:
    """
    Gestion d'employés
    """
    def __init__(self,matricule, nom, prenom, dateNaissance, dateEmbauche, salaire):

        self.pseudo, self.nom, self.prenom = matricule, nom, prenom
        self.birthDate, self.employmentDate, self.salaire = dateNaissance, dateEmbauche, salaire

    def age(self):

        return annee - self.birthDate[2]

    def anciennete(self):

        return annee - self.employmentDate[2]

    def augmentationDuSalaire(self):

        if self.anciennete() < 5:
            self.salaire *= 1.02
        elif self.anciennete() < 10:
            self.salaire *= 1.05
        else:
            self.salaire *= 1.10

    def afficherEmploye(self):

        print(f"Matricule: {self.pseudo}\nNom: {self.nom}\nPrénom: {self.prenom}\nAge: {self.age()}\nAncienneté: {self.anciennete()}\nSalaire en €: {self.salaire}")

#test de la classe Employe
agent=Employe('007','Bond','James',(11,11,1970),(7,4,1995),7500)
agent.augmentationDuSalaire()
agent.afficherEmploye()