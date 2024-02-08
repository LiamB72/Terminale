from utilityModule import File, creerArbre

def taille(arbre):
    if not arbre:
        return 0

    left = taille(arbre.left)
    right = taille(arbre.right)
    return 1 + left + right

tree = creerArbre()
print(tree)
print(f"taille: {taille(tree)}")