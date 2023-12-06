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


def bien_parenthese(txt):
    verificateur = True
    p = Pile()
    indice = 0
    
    while verificateur==True and indice < len(txt):
        
        if txt[indice] == "(":
            p.empiler(txt[indice])
            
        elif txt[indice] == ")":
            if p.sommet() != "(":
                verificateur = False
            else:
                p.depiler()
            
        indice = indice+1
            
    if p.estVide()==False:
        verificateur = False
    return True
print(bien_parenthese("(3+2)+5*(2+8)"))
print(bien_parenthese("(3+2)+5*(2+8"))
