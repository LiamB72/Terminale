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

#((4/3) * pi) * (r ** 3)  <==>  (4* pi / 3) * (r ** 3)

doctest.testmod()

volumeSpheres = 0
volumeCylinder = round(volumeRecipient(30, 58))
wtarVolume = round(volumeRecipient(30, 50))

i = 0

while wtarVolume < volumeCylinder:
    i += 1
    volumeSpheres = round(volumeSphere(i))
    wtarVolume += volumeSpheres
    print(f"{i:3} Spheres Volume: {volumeSpheres:4}, waterVolume: {wtarVolume}")

print(f"\nIl faut {i} Sphères pour remplir le contenaire de {volumeCylinder}")
