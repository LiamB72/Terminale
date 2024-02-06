def depouille(lst:list):
    
    d = {}
    
    for element in lst:
        
        if element in d:
            d[element] += 1
        else:
            d[element] = 1
            
    print(f"election: {d}")
    return d


def vainqueur(election):
    vainqueur = ''
    nmax = 0
    lst_Election = list(election.items())
    for i in range(len(lst_Election)-1):
        
        if lst_Election[i][1] > lst_Election[i + 1][1]:
            
            vainqueur = lst_Election[i][0]
            nmax = lst_Election[i][1]
        
    
    liste_finale = [nom for nom in election if election[nom] == nmax]
    print(liste_finale)
    return vainqueur

Urne = ['A', 'A', 'A', 'B', 'C', 'B', 'C', 'B', 'C', 'B']

election = depouille(Urne) # a0 {'B': 4, 'A': 3, 'C': 3}
vainqueur(election) # ['B']