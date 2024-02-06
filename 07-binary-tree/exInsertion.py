from utilityModule import *

def insertion(arb, cle):
    if not arb:
        return False

    x = arb.value

    if cle < x:
        return  Node(value=x, left=insertion(arb.left, cle), right=arb.right)
    else:
        return Node(value=x, left=arb.left, right=insertion(arb.right, cle))

abr = creerBST()
print("Arbre avant insertion",abr)
abr=insertion(abr, 5)
# print("Arbre après insertion",abr)