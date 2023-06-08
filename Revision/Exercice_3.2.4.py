#Exercices 3

#3.2.4 :

def triangleDef(a, b, c):
   if (a == b and a == c and c == b):
      print("Ton triangle est équilatéral")
   if (a == b or a == c or c == b) and not (a == b and a == c and c == b):
      print("Ton triangle est isolcèle")
   if not (a == b or a == c or c == b) and not (a == b and a == c and c == b):
      print("Ton triangle est quelconque")

a = int(input("Longueur segment A : "))
b = int(input("Longueur segment B : "))
c = int(input("Longueur segment C : "))

triangleDef(a,b,c)