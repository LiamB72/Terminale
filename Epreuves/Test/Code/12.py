def positif(pile):
    ogPile = list(pile)
    tempPile = []
    i = 0
    while ogPile != []:
        
        x = ogPile.pop()
        
        if x >= 0:
            tempPile.append(x)
            
    while tempPile != []:
        x = tempPile.pop()
        ogPile.append(x)
        
    return ogPile

positif([-1, 0, 5, -3, 4, -6, 10, 9, -8])
positif([-2])