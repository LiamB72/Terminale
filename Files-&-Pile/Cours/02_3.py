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


p = Pile()

p.empiler('A')
p.empiler('B')
p.empiler('C')
p.empiler('D')

out = Pile()
for i in range(3):
    out.empiler(p.depiler())
    
element = out.depiler()

for i in range(2):
    p.empiler(out.depiler())
    
print("3ème élément :", element)
print(p)
