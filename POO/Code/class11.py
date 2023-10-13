from math import pi,sqrt


class Cercle:
    """
    Calculs du périmètre et de l'aire d'un cercle.
    test d'appartenance à un point
    """

    def __init__(self, A, rayon):

        self.centre = (A[0], A[1])
        self.rayon = rayon

    def aire(self):

        return pi*(self.rayon**2)

    def perimetre(self):

        return (self.rayon*2)*pi

    def testAppartenance(self, A):
        x_point, y_point = A[0], A[1]
        x_centre, y_centre = self.centre[0], self.centre[1]

        if sqrt((x_point - x_centre)**2 + (y_point - y_centre)**2) <= self.rayon:
            testCheck = True
        else:
            testCheck = False

        return testCheck

    def __repr__(self):

        return f"P = {str(self.perimetre())}\nA = {str(self.aire())}"

#test de la classe Cercle
c1=Cercle((2,2),3)
print(c1)
print(c1.testAppartenance((0,0)))
print(c1.testAppartenance((0,-1)))
