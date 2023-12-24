"""
fonction inverse (chaine : chaine de caractères) :chaine
	si longueur(chaine)=0 alors
		retourner chaine vide
	sinon
		retourner inverse(...) + ...
	fin si

affiche(inverse (« hello »))
"""

def inverse(string:str) -> str:
    
    if len(string) == 0:
        return ""
    
    else:
        return inverse(string[1:]) + string[0]
    
print(inverse("hello"))