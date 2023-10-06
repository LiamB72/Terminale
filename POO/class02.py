class c():

    def __init__(self, l):

        self.length = l

    def area(self):

        return self.length**2

    def perimeter(self):

        return self.length*4

    def __repr__(self):

        return str(self.length)
x=5
c1 = c(x)

print(f"Square of length: {x}\nArea: {c1.area()}\nPerimeter: {c1.perimeter()}")
