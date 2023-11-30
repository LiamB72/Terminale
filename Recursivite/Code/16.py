"""
fonction recherche(lst : liste, x entier) : booleen
	si longueur(lst)=0 alors
		retourner faux
	fin si
	m←longueur(lst) //2
	si lst[m]=x alors
		retourner vrai
	sinon si x>lst[m]:
			retourner recherche(lst[:m],x)
		sinon
			retourner recherche(lst[m+1:],x)
		fin si
	fin si

lst=[2,5,9,12,15,21,34]

affiche(recherche(lst,4))
affiche(recherche(lst,12))
"""

def recherche(lst:list, x:int) -> bool:
    
    if len(lst) == 0:
        return False
    
    middle = len(lst)//2
    if lst[middle] == x:
        return True
    elif x > lst[middle]:
        return recherche(lst[:middle], x)
    else:
        return recherche(lst[middle+1:], x)

lst=[2,5,9,12,15,21,34]

print(recherche(lst,4))
print(recherche(lst,12))