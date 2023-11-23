def depouille(lst:list):
    
    d = {}
    
    for element in range(len(lst)):
        
        d[element] = d[element] + 1
def vainqueur(election):
    vainqueur = ''
    nmax = 0
    for candidat in election:
        if ... > ... :
            nmax = ...
            vainqueur = candidat
    
    liste_finale = [nom for nom in election if election[nom] == ...]
    return 

Urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']

election = depouille(Urne)
# election {'B': 4, 'A': 3, 'C': 3}
vainqueur(election) # ['B']