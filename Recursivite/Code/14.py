"""
fonction pgcd(a :entier, b :entier) : entier
	si b=0 alors
		retourner a
	sinon
		retourner pgcd(b,a modulo b)
	fin si

affiche(pgcd (21,15))
"""

def pgcd(a0:int, a1:int) -> int:
    
    if a1 == 0:
        return a0
    else:
        return pgcd(a1, a0%a1)
    
print(pgcd(21, 15))