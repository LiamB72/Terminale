### Ex:1

def recherche(character: str, string: str):
    total = 0

    for i in range(len(string)):

        if character == string[i]:
            total += 1

    return total


assert recherche('e', "sciences") == 2
assert recherche('i', "mississippi") == 4
assert recherche('a', "mississippi") == 0

### Ex:2

values = [100, 50, 20, 10, 5, 2, 1]


def rendu_glouton(a_rendre:int, rang:int) -> list:
    if a_rendre == 0:
        return []
    v = values[rang]
    if v <= a_rendre:
        return [v] + rendu_glouton(a_rendre - v, rang)
    else:
        return rendu_glouton(a_rendre, rang - 1)


print(rendu_glouton(67,  0))
print(rendu_glouton(291, 0))
print(rendu_glouton(291, 1))