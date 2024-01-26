def recherche(a0: list, a1: int)s:
    indexReturned = None
    for i in range(len(a0)):
        if a1 == a0[i]:
            indexReturned = i

    return len(a0) if indexReturned is None else indexReturned


print(recherche([5, 3], 1))  # 2
print(recherche([2, 4], 2))  # 0
print(recherche([2, 3, 5, 2, 4], 2))  # 3
