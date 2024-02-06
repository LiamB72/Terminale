from utilityModule import *

def recherche(arb,cle):
    if arb:
        return False
    x = arb.value
    if cle == x:
        return True
    else:
        if cle < x:
            return recherche(arb.left, cle)
        else:
            return recherche(arb.right, cle)

arb = bst(height=3)
print(arb)
print(recherche(arb, 4))