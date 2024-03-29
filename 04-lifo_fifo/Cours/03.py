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


def bien_parentheses(txt):
    verification = True
    p = Pile()
    index = 0
    
    while verification and index < len(txt):
        
        if txt[index] == "(":
            p.empiler(txt[index])
            
        elif txt[index] == ")":
            if p.sommet() != "(":
                verification = False
            else:
                p.depiler()
            
        index = index + 1
            
    if not p.estVide():
        verification = False
    return verification


print(bien_parentheses("(3+2)+5*(2+8)"))
print(bien_parentheses("(3+2)+5*(2+8"))
