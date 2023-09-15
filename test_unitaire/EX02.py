"""
Fonction linéaire
"""
import doctest
def fctLineaire(x):
    """
    fonction lineaire
    retourne le résultat de 2x
    Argument:
    x -- nombre
    >>> fctLineaire(2)
    4
    >>> fctLineaire(5)
    12
    """
    return x * 2

doctest.testmod()
