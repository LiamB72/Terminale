def affichage(n):
    if n <= 0:
        print(n,"Terminé")
    else:
        print(n,"hello")
        affichage(n-1)

affichage(5)
affichage(-3)