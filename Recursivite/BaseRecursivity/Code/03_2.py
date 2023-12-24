def afficheDEC_REC(n):
    if n==0:
        print(n)
    else:
        print(n)
        afficheDEC_REC(n-1)

afficheDEC_REC(5)