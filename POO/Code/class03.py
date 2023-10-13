class c():
    def __init__(self, l, h):
        self.length = l
        self.height = h

    def area(self):
        return self.length*self.height

    def perimeter(self):
        return (self.length+self.height)*2

    def __repr__(self):
        return str(self.length)

length=5
height=10
c1 = c(length,height)

print(f"Largeur: {length} || Hauteur: {height}")
print(f"Area: {c1.area()}\nPerimeter: {c1.perimeter()}")