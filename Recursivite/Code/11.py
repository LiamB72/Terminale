# fonction factorielle(n : entier) : entier
# 	affiche(« fact »,n)
# 	si n=0 alors
# 		retourner 1
# 	sinon
# 		retourner n*factorielle(n-1)
# 	fin si

# affiche(factorielle(5))

def fact(n:int) -> int:
    
    print("fact", n)
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))