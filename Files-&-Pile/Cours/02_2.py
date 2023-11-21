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
p2 = Pile()

p.empiler('A')
p.empiler('B')
p.empiler('C')
print(p)

for i in range(2):
    p2.empiler(p.depiler)
    p.empiler(p2.depiler)

print(p)