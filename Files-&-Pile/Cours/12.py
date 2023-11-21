def creer():
    queue = []
    return queue


def longueur(queue):
    return len(queue)


def enfiler(queue, avion):
    queue.append(avion)


def defiler(queue):
    avion = None
    indicePrioritaire = 0
    if not estvide(queue):
        for indice in range(0, len(queue)):
            if queue[indice][0] < queue[indicePrioritaire][0]:
                indicePrioritaire = indice

        avion = queue[indicePrioritaire]

        del queue[indicePrioritaire]

    return avion

def estvide(queue):
    if len(queue) == 0:
        return True
    else:
        return False


queue = creer()
enfiler(queue, (3, 'LH713'))
enfiler(queue, (3, 'HP856'))
enfiler(queue, (3, 'FR1745'))
enfiler(queue, (0, 'AF644'))
print(queue)
print('La liste est vide ?', estvide(queue))
print('La longueur de la liste est :', longueur(queue))
print(defiler(queue))
print(defiler(queue))
print(defiler(queue))
print(defiler(queue))
print('La liste est vide ?', estvide(queue))
print('La longueur de la liste est :', longueur(queue))
