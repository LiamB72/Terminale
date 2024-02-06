from binarytree import bst, Node, tree

class Pile:
    def __init__(self):
        self.pile = []

    def __len__(self):
        return len(self.pile)

    def __repr__(self):
        return ' '.join([str(i) for i in self.pile])

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        return self.pile.pop()

    def estVide(self):
        if len(self.pile) == 0:
            return True
        return False

    def sommet(self):
        if not self.estVide():
            return self.pile[-1]

class File:
    def __init__(self):
        self.file = []

    def __len__(self):
        return len(self.file)

    def __repr__(self):
        return ' '.join([str(i) for i in self.file])

    def enfiler(self, avion):
        self.file.append(avion)

    def defiler(self):
        return self.file.pop(0)

    def estVide(self):
        vide=False
        if not self.file:
            vide=True
        return vide

def creerArbre():
    arbre = Node(1)
    arbre.left = Node(2)
    arbre.left.left = Node(4)
    arbre.left.right = Node(5)
    arbre.left.right.left = Node(7)
    arbre.left.right.right = Node(8)

    arbre.right = Node(3)
    arbre.right.right = Node(6)
    arbre.right.right.left = Node(9)

    return arbre

def creerBST():

    arb = Node(10)
    arb.left = Node(3)
    arb.left.left = Node(1)
    arb.left.right = Node(7)

    arb.right = Node(20)
    arb.right.left = Node(15)
    arb.right.left.left = Node(11)
    arb.right.left.right = Node(17)
    arb.right.right = Node(25)
    arb.right.right.left = Node(21)
    arb.right.right.left.right = Node(24)

    return arb

def prefixPath(arbre):
    print(arbre.value, end=',')
    if arbre.left:
        prefixPath(arbre.left)
    if arbre.right:
        (prefixPath(arbre.right))

def infixPath(arbre):
    if arbre.left:
        infixPath(arbre.left)
    print(arbre.value, end=',')
    if arbre.right:
        infixPath(arbre.right)

def subfixPath(arbre):
    if arbre.left:
        subfixPath(arbre.left)
    if arbre.right:
        subfixPath(arbre.right)
    print(arbre.value, end=',')