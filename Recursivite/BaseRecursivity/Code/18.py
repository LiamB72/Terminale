"""fonction puissance(a :entier, n : entier) : entier
	si n= ... alors
		retourner ...
	sinon
		retourner ...
	fin si

affiche(puissance(2,4))"""

def expo(a:int, n:int) -> int:
    
    if n == 0:
        return 1
    
    else:
        return a * expo(a, n-1)
    
print(expo(3,3))
