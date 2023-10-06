class point():

    def __init__(self, abscisse, ordonnee):
        self.x, self.y = abscisse, ordonnee

    def trannslattee(self, dx, dy):

        self.x += dx
        self.y += dy

    def homothetie(self, k):
        #self.x *= k
        #self.y *= k

        self.x, self.y = self.x*k, self.y*k

    def __repr__(self):
        return f"{self.x} {self.y}"

p = point(3, 4)

print(p)

p.homothetie(2)

print(p)