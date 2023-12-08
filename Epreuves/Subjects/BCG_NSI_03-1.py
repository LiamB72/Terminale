def moyenne(lst: list):
    res = 0
    coef = 0
    for elements in lst:

        for i in range(2):
            res += elements[0] * elements[1]
            coef += elements[1]

    if coef == 0:
        return None

    else:
        return res / coef


assert moyenne([(8, 2), (12, 0), (13.5, 1), (5, 0.5)]) == 9.142857142857142
assert moyenne([(3, 0), (5, 0)]) == None