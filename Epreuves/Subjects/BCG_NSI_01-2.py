urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(a0):
    resultat = {}
    for bulletin in a0:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1

    return resultat


def vainqueur(a0):
    nmax = 0
    for candidat in a0:
        if a0[candidat] > nmax:
            nmax = a0[candidat]
    liste_finale = [nom for nom in a0 if a0[nom] == nmax]
    return liste_finale


election = depouille(urne)
print(vainqueur(election))
