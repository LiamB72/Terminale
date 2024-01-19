from random import randint

def lancer(n):
    returnedList = []
    for i in range(n):

        returnedList.append(randint(1,6))

    return returnedList

def paire_6(tab:list) -> bool:

    total = 0

    for i in range(len(tab)):
        if tab[i] == 6:
            total += 1

    if total >= 2:
        return True

    return False

lancer = lancer(6)
print(lancer)
print(paire_6(lancer))
