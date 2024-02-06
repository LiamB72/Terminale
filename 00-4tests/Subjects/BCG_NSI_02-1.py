def indices_maxi(lst: list):
    maxNb = lst[0]
    nbOccurrences = []
    for i in range(len(lst)):
        if lst[i] > maxNb:
            maxNb = lst[i]

    for j in range(len(lst)):
        if lst[j] == maxNb:
            nbOccurrences.append(j)
    return maxNb, nbOccurrences


assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, [3, 8])
assert indices_maxi([7]) == (7, [0])
