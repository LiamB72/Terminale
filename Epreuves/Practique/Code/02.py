from math import sqrt

def distance(point1:tuple, point2:tuple):
    
    return sqrt(((point1[0]-point2[0])**2) + ((point1[1]-point2[1])**2))

assert distance((1, 0), (5, 3)) == 5.0, "erreur de calcul"

def plus_courte_distance(tab, depart):
    """ Renvoie le point du tableau tab se trouvant à la plus courte distance du point depart."""
    
    point = tab[0]
    min_dist = distance(point, depart)
    
    for i in range (1, len(tab)):
        
        if distance(tab[i], depart) < min_dist:
            
            point = list(tab[i])
            min_dist = distance(point, depart)  
            
    return point

assert plus_courte_distance([(7, 9), (2, 5), (5, 2)], (0, 0)) == [2, 5], "erreur"