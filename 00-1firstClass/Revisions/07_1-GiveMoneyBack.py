def renduMonnaie(somme,pieces):
    choisies={}
    for p in pieces:
        nb = somme // p
        choisies[p] = nb
        somme = somme - nb * p
    return choisies

pieces=[500,200,100,50,20,10,5,2,1]
somme=500

print(renduMonnaie(somme,pieces))