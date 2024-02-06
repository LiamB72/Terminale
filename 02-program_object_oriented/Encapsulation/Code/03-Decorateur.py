class Point:
    """
    Manipulation de points.
    """
    def __init__(self, abscisse, ordonnee):
        """
        Initialise le point avec les coordonnées indiquées
        """
        self.__x, self.__y = abscisse, ordonnee

    @property
    def x(self):
        """
        lecture de l'attribut _x
        """
        return self.__x

    @property
    def y(self):
        """
        lecture de l'attribut _y
        """
        return self.__y

    @x.setter
    def x(self, x):
        """
        modiification de l'attribut _x
        """
        self.__x = x

    @y.setter
    def y(self, y):
        """
        modiification de l'attribut _y
        """
        self.__y = y

p = Point(3, 7)
print("Cordonnées du point A avant la méthode set():")
print("\t\tA : abscisse =", p.x, "ordonnée =", p.y)
p.x=6
p.y=10
print("Cordonnées du point A après la méthode set():")
print("\t\tA : abscisse =", p.x, "ordonnée =", p.y)