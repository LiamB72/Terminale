def verifie(lst:list) -> bool:

    if len(lst) > 1 :
        for i in range(len(lst)-1):
            if lst[i] > lst[i + 1]:
                return False

    return True


print(verifie([0, 5, 8, 8, 9]))
print(verifie([8, 12, 4]))
print(verifie([-1, 4]))
print(verifie([5]))