from utilityModule import File, creerArbre

def lenghtPath(arbre):
    f = File()
    f.enfiler(arbre)
    while f:
        noeud = f.defiler()
        print(noeud.value, end=',')
        if noeud.left:
            f.enfiler(noeud.left)
        if noeud.right:
            f.enfiler(noeud.right)

tree = creerArbre()
print(tree)
print(lenghtPath(tree))