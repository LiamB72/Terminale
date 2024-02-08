from utilityModule import *

def insertionArbre(arbre, cle):
    if not arbre:
        return Node(cle)

    x = arbre.value

    if cle < x:
        return Node(value=x,
                    left=insertionArbre(arbre.left, cle),
                    right=arbre.right)
    else:
        return Node(value=x,
                    left=arbre.left,
                    right=insertionArbre(arbre.right, cle))

abr = bst(height=3)
print("Arbre avant insertion",abr)
abr=insertionArbre(abr, 5)
print("Arbre après insertion",abr)