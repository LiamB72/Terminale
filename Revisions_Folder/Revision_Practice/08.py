import numpy as np
import matplotlib.pyplot as plt
import sympy as symp

a = float(input("a = "))
b = float(input("b = "))

c = float(input("a' = "))
d = float(input("b' = "))

x = symp.symbols('x')

if not (a == 0 or b == 0) or (c == 0 or d == 0):
    D_1 = a * x + b
    D_2 = c * x + d


    if a == c and b == d:
        print(f"Both {D_1} and {D_2} are equal.")

    else:
        if a == c and b != d:
            print("Les deux droites sont distinces mais parallèles")

        if a != c:
            print("Les droites sont sécantes au point I = ", end='')
            x = (d - b)/(a-c)
            y = a * x + b

            print(f"(x : {round(x,2)})")
            print(f"\t\t\t\t\t\t\t\t      (y : {round(y,2)})")

x = np.linspace(-100, 100, 500)

y1 = a * x + b
y2 = c * x + d

plt.plot(x, y1, label="y1", color="blue")
plt.plot(x, y2, label="y2", color="red")

plt.title(f"Crossing Lines")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.grid(True)
plt.legend()
plt.show()