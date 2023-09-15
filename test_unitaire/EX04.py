"""
calcul la surface d'un disque en fonction du rayon
"""
import doctest
from math import pi
def surfaceDisque(rayon):
    """
    fonction qui retourne la surface d'un disque en fonction du rayon
    argument:
    rayon -- nombre
    >>> surfaceDisque(5)
    78.53981633974483
    """

    return pi*rayon**2
print(surfaceDisque(5))
doctest.testmod()
