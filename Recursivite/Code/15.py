"""
fonction fibo(n :entier) : entier
	si n< ... alors
		retourner #a compléter
	sinon
		retourner #a compléter
	fin si

affiche(fibo (10))
"""

def fibo(n:int) -> int:
    if n <= 0:
        return n
    else:
        return abs(fibo(n-1) + fibo(n-2))
    
print(fibo(10))