urne = ['A', 'A', 'A','B', 'C', 'B', 'C','B', 'C', 'B']

def depouille(urne):
    resultat = {}
    for bulletin in urne:
        if bulletin in resultat:
            resultat[bulletin] = resultat[bulletin] + 1
        else:
            resultat[bulletin] = 1

    return resultat


def vainqueur(election):
    vainqueur = ''
    nmax = 0
    lst_Election = list(election.items())
    for i in range(len(lst_Election) - 1):

        if lst_Election[i][1] > lst_Election[i + 1][1]:
            vainqueur = lst_Election[i][0]
            nmax = lst_Election[i][1]

    liste_finale = [nom for nom in election if election[nom] == nmax]
    print(liste_finale)
    return vainqueur


election = depouille(urne)
print(election)
vainqueur(election)
