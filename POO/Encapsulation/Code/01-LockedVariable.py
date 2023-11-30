"""
class Point:
    
    Manipulation de points.

    def __init__(self, abscisse, ordonnee):
        
        Initialise le point avec les coordonnées indiquées
        
        self.x, self.y = abscisse, ordonnee

    def translater(self, dx, dy):
        
        Translate le point selon le vecteur (dx,dy)
        
        self.x += dx
        self.y += dy


p=Point(8,18)
print("A( ",p.x," , ",p.y," )")
"""
# ---> A(  8  ,  18  )


class Point:
    
    # Manipulation de points.
    

    def __init__(self, abscisse, ordonnee):
        
        # Initialise le point avec les coordonnées indiquées
        
        self.__x, self.__y = abscisse, ordonnee

    def translater(self, dx, dy):
        
        # Translate le point selon le vecteur (dx,dy)
        
        self.__x += dx
        self.__y += dy


p=Point(8,18)
print("A( ",p.__x," , ",p.__y," )")

# print("A( ",p.__x," , ",p.__y," )")
# AttributeError: 'Point' object has no attribute '__x'