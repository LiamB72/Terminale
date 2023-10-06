import time
from math import *

import doctest

class equationSolver():
    def __init__(self, a, b ,c):

        self.a = a
        self.b = b
        self.c = c

        while True:

            self.inputAsk()

            if self.b < 0 and self.c < 0:
                print(f"\n\nCurrent Equation :\n\nf(x) = {self.a}x²{self.b}x{self.c}\n\n")
            elif self.b < 0:
                print(f"\n\nCurrent Equation :\n\nf(x) = {self.a}x²{self.b}x+{self.c}\n\n")
            elif self.c < 0:
                print(f"\n\nCurrent Equation :\n\nf(x) = {self.a}x²+{self.b}x{self.c}\n\n")
            else:
                print(f"\n\nCurrent Equation :\n\nf(x) = {self.a}x²+{self.b}x+{self.c}\n\n")

            time.sleep(1)

            self.calculateDelta()

            time.sleep(1)

            self.calculateSolutions()

            break

    def inputAsk(self):
        #self.a = float(input("a = "))
        #self.b = float(input("b = "))
        #self.c = float(input("c = "))

        if self.a < 0:
            self.fakeA = f"({self.a})"
        if self.b < 0:
            self.fakeB = f"({self.b})"
        if self.a < 0:
            self.fakeC = f"({self.c})"

        print("\n<<------------------>>")

    def calculateDelta(self):
        print("<<------------------>>\n\nΔ = b² - 4 * a * c")

        """
        >>>equationSolver(-8,-6,7).calculate()
        <<------------------>>

        Δ = b² - 4 * a * c

        Δ = (-6.0)² - 4 * (-8.0) * 7.0

        Δ = 260.00

        <<------------------>>
        """

        self.delta = self.b**2 - 4 * self.a * self.c

        if self.b < 0 and self.c < 0 and self.a:
            print(f"\nΔ = ({self.b})² - 4 * ({self.a}) * ({self.c})")

        elif self.b < 0 and self.a < 0:
            print(f"\nΔ = ({self.b})² - 4 * ({self.a}) * {self.c}")
        elif self.a < 0 and self.c < 0:
            print(f"\nΔ = {self.b}² - 4 * ({self.a}) * ({self.c})")
        elif self.c < 0 and self.b < 0:
            print(f"\nΔ = ({self.b})² - 4 * {self.a} * ({self.c})")

        elif self.b < 0:
            print(f"\nΔ = ({self.b})² - 4 * {self.a} * {self.c}")
        elif self.a < 0:
            print(f"\nΔ = {self.b}² - 4 * ({self.a}) * {self.c}")
        elif self.c < 0:
            print(f"\nΔ = {self.b}² - 4 * {self.a} * ({self.c})")

        else:
            print(f"\nΔ = {self.b}² - 4 * {self.a} * {self.c}")


        print(f"\nΔ = {self.delta:.2f}\n\n<<------------------>>\n\n")

    def calculateSolutions(self):
        if self.delta > 0:
            print(f"Possible Solutions : x1; x2\n")

            self.x1 = (-(self.b)-sqrt(self.delta))/(2 * self.a)
            self.x2 = (-(self.b)+sqrt(self.delta))/(2 * self.a)

            print(f"\nx1 = (-({self.b}) - sqrt({self.delta})) / (2 * ({self.a}))\n")
            print(f"\nx1 = {self.x1:.2f}\n")
            print(f"\nx2 = (-({self.b}) + sqrt({self.delta})) / (2 * ({self.a}))\n")
            print(f"\nx2 = {self.x2:.2f}\n")
            print("<<----------------->>")

        if self.delta == 0:
            print(f"Possible Solution : x0\n")

            self.x0 = (-self.b)/(2 * self.a)

            print(f"\nx0 = α")
            print(f"\nα  = -b / 2 * a")
            print(f"\nx0 = -b / 2 * a")
            print(f"\nx0 = -({self.b}) / 2 * ({self.a})")
            print(f"\nx0 = {self.x0:.2f}\n")

        if self.delta < 0:
            print(f"Possible Solution : None")

#equationSolver()

doctest.testmod()