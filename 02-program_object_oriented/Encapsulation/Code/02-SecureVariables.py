class Point:
    """
    Manipulation de points.
    """
    def __init__(self, abscisse, ordonnee):
        """
        Initialise le point avec les coordonnées indiquées
        """
        self.__x, self.__y = abscisse, ordonnee
    def get_x(self):
        """
        lecture de l'attribut _x
        """
        return self.__x
    def get_y(self):
        """
        lecture de l'attribut _y
        """
        return self.__y
    def set_x(self, x):
        """
        modiification de l'attribut _x
        """
        self.__x = x
    def set_y(self, y):
        """
        modiification de l'attribut _y
        """
        self.__y = y

p = Point(3, 7)
print("Cordonnées du point A avant la méthode set():")
print("\t\tA : abscisse =", p.get_x(), "ordonnée =", p.get_y())
p.set_x(6)
p.set_y(10)
print("Cordonnées du point A après la méthode set():")
print("\t\tA : abscisse =", p.get_x(), "ordonnée =", p.get_y())

# Cordonnées du point A avant la méthode set():
# A : abscisse = 3 ordonnée = 7
# Cordonnées du point A après la méthode set():
# A : abscisse = 6 ordonnée = 10