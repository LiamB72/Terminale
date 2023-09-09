import sympy

a = float(input("a = "))
b = float(input("b = "))

c = float(input("a' = "))
d = float(input("b' = "))

x = sympy.symbols('x')

if not (a == 0 or b == 0) or (c == 0 or d == 0):
    D_1 = a * x + b
    D_2 = c * x + d


    if a == c and b == d:
        print(f"Both {D_1} and {D_2} are equal.")
        
    else:
        if a == c and b != d:
            print("Les deux droites sont distinces mais parallèles")
            
        if a != c:
            print("Les droites sont sécantes en :")
            x = (d - b)/(a-c)
            y = a * x + b
            print(f'x = {x}, y = {y}')