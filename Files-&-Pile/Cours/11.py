def creer():
    enAttente = []
    return enAttente


def longueur(enAttente):
    return len(enAttente)


def enfiler(enAttente,avion):
    enAttente.append(avion)


def defiler(enAttente):
    return enAttente.pop(0)


def estVide(enAttente):
    if len(enAttente) == 0:
        return True
    else:
        return False


enAttente = creer()
enfiler(enAttente,'LH713')
enfiler(enAttente,'HP856')
enfiler(enAttente,'FR1745')
enfiler(enAttente,'AF644')
print(enAttente)
print('La liste est vide ?',estVide(enAttente))
print('La longueur de la liste est :',longueur(enAttente))
print(defiler(enAttente))
print(defiler(enAttente))
print(defiler(enAttente))
print(defiler(enAttente))
print('La liste est vide ?',estVide(enAttente))
print('La longueur de la liste est :',longueur(enAttente))
