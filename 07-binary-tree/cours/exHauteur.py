from utilityModule import File, creerArbre

def hauteur(arbre):
    if not arbre:
        return 0

    left = hauteur(arbre.left)
    right = hauteur(arbre.right)
    return 1 + max(left, right)

tree = creerArbre()
print(tree)