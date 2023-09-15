from math import pi
import doctest

def volumeRecipient(r, h):
    """
    >>> volumeRecipient(30, 58)
    163991.1365173872
    """
    return pi * (r ** 2) * h

def volumeSphere(r):

    """
    >>> volumeSphere(1)
    4.1887902047863905
    """

    return ((4/3) * pi) * (r ** 3)

doctest.testmod()

volumeSpheres = 0
volumeCylinder = round(volumeRecipient(30, 58))

for i in range(1,31):
    if volumeSpheres < volumeCylinder:
        volumeSpheres += round(volumeSphere(i))
        print(volumeSpheres)
    else:
        print(f"Il faut {i-1} Sphères pour remplir le contenaire de {volumeCylinder}")
        break



