class Domino:
    """
    simulateur de domino
    """

    def __init__(self, a, b):

        self.faceA = a
        self.faceB = b

    def affichePoints(self):

        print(f"Face A : {self.faceA}, Face B : {self.faceB}")

    def valeur(self):
        return self.faceA+self.faceB

    def __repr__(self):
        a = (self.faceA, self.faceB)
        return f"Domino : {a}"


#test de la clsse Domino
d1=Domino(2,6)
d2=Domino(4,3)
d1.affichePoints()
d2.affichePoints()
print("total des points :", d1.valeur() + d2.valeur())
print(d1)
