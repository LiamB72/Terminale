def moyenne(liste:tuple):
    
    total = 0
    moy = 0
    
    if len(liste) != 0:
        for i in range(len(liste)):
            
            total += liste[i]
        
        moy = total/len(liste)
        print(moy)
        
    else:
        
        print("erreur")

moyenne([5,3,8])
moyenne([1,2,3,4,5,6,7,8,9,10])
moyenne([])
