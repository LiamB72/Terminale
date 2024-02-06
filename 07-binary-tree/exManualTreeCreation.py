from binarytree import Node, tree

# Créer un arbre manuellement
def creerArbre():
    arbre = Node(4)
    arbre.left = Node(5)
    arbre.right = Node(6)

    arbre.left.left = Node(1)
    arbre.left.right = Node(10)
    arbre.right.left = Node(7)
    arbre.right.right = Node(4)

    arbre.left.left.left = Node(3)
    arbre.left.right.right = Node(9)
    arbre.right.left.left = Node(12)
    arbre.right.right.left = Node(20)

    arbre.right.left.left.left = Node(15)
    return arbre

arbre=creerArbre()
print("Arbre crée à la main")
print(arbre)