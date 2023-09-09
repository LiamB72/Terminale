tab=[5,9,2,3,6,10,13,45,7]

def infoList(list):
    
    lenght = len(list)
    somme = 0
    
    for i in range(lenght):
        somme += list[i]
        
    moyenne = somme / lenght
    
    return somme, moyenne

somme_tab, moy_tab = infoList(tab)

print(f"La somme total de tab est : {somme_tab}\nLa moyenne de tab est : {moy_tab:.2f}")