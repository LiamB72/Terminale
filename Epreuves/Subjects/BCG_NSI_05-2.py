img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]


def nbLig(img):
    '''renvoie le nombre de lignes de l'image'''
    return len(img)


def nbCol(img):
    '''renvoie la largeur de l'image'''
    return len(img[0])


def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]
    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            L[i][j] = 255 - image[i][j]
    return L


def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil
       et 1 sinon'''

    # on cree une image de 0 aux memes dimensions que le parametre image
    L = [[0 for k in range(nbCol(image))] for i in range(nbLig(image))]

    for i in range(nbLig(image)):
        for j in range(nbCol(image)):
            if image[i][j] < seuil:
                L[i][j] = 0
            else:
                L[i][j] = 1
    return L


img = [[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
print(nbLig(img))
print(nbCol(img))
print(negatif(img))
print(binaire(img, 120))
# 4
# 5
# [[235, 221, 1, 110, 249], [232, 131, 18, 30, 186], [58, 81, 48, 230,168], [0, 255, 231, 58, 66]]
# [[0, 0, 1, 1, 0], [0, 1, 1, 1, 0], [1, 1, 1, 0, 0], [1, 0, 0, 1, 1]]
