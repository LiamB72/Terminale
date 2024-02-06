bombes = [(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)]
grille_test = [[1, 1, 1, 0, 0], [1, -1, 1, 1, 1], [2, 2, 3, 2, -1], [1, -1, 2, -1, 3], [1, 1, 2, 2, -1]]


def voisinage(n, ligne, colonne):
    voisins = []
    for l in range(max(0, ligne - 1), min(n, ligne + 2)):
        for c in range(max(0, colonne - 1), min(n, colonne + 2)):
            if (l, c) != (ligne, colonne):
                voisins.append((l, c))
    return voisins


def incremente_voisins(grille, ligne, colonne):
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1:  # si ce n'est pas une bombe
            grille[l][c] += 1  # on ajoute 1 à sa valeur


def genere_grille(bombs):
    n = len(bombs)
    # Initialisation d'une grille nxn remplie de 0
    grille = [[0 for colonne in range(n)] for ligne in range(n)]

    # Place les bombs et calcule les valeurs des autres cases
    for ligne, colonne in bombs:
        grille[ligne][colonne] = -1  # place la bombe
        incremente_voisins(grille, ligne, colonne)  # incrémente ses voisins

    return grille


grid = genere_grille([(1, 1), (2, 4), (3, 1), (3, 3), (4, 4)])

for i in range(len(grid)):
    print(grid[i])
