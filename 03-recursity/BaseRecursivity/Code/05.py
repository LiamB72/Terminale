import sys

taille = sys.getrecursionlimit()
print('Taille de la pile =', taille)

NouvelleTaille = 300
sys.setrecursionlimit(NouvelleTaille)