def afficheINC_REC(n):
    if n==0:
        print(n)
    else:
        afficheINC_REC(n-1)
        print(n)

afficheINC_REC(5)
