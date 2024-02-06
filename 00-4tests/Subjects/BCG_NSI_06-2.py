from math import sqrt  # import de la fonction racine carree


def distance(point1: tuple, point2: tuple) -> float:
    """ Calcule et renvoie la distance entre deux points. """
    return sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def plus_courte_distance(tab: list, depart: tuple) -> tuple:
    """ Renvoie le point du tableau tab se trouvant a la plus
    courte distance du point depart."""
    point = tab[0]
    min_dist = distance(point, depart)
    for i in range(1, len(tab)):
        if distance(tab[i], depart) < min_dist:
            point = tab[i]
            min_dist = distance(tab[i], depart)
    return point


print(distance((1, 0), (5, 3)))  # 5.0
print(distance((1, 0), (0, 1)))  # 1.4142135623730951
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)))  # (2, 5)
print(plus_courte_distance([(7, 9), (2, 5), (5, 2)], (5, 2)))  # (5, 2)
