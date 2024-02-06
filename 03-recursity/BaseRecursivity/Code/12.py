"""
fonction genereDecrementation_rec (n : entier) :liste
	si n=0 alors
		retourner #a compléter
	sinon
		retourner #a compléter
	fin si

affiche(genereDecrementation_rec (10))
"""

def lstDec(n:int) -> int:
    
    if n == 0:
        return [n]
    else:
        return [n] + lstDec(n-1)
    
print(lstDec(10))