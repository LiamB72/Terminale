

def recherche(tableau, n):
    
    number_searched = n
    lastIndex = 0
    tab = tableau
    
    found = False
    
    lenght_tab = len(tab)
    
    for i in range(lenght_tab):
        
        if tab[i] == number_searched:
            
            found = True
            lastIndex = i
            
    if found:
        
        return lastIndex
    
    else:
        return lenght_tab

print(recherche([5, 3],1))
print(recherche([2,4],2))
print(recherche([2,3,5,2,4],2))