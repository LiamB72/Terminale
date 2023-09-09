tab=[5,9,2,3,6,10,13,45,7]

def lookout(number):
    for i in range(len(tab)):
        if tab[i] == number:
            nIndex = i
            break
    return nIndex

print(lookout(10))