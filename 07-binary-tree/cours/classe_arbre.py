class ArbreBinaire:
    """
    Classe permettant de construire un arbre binaire de recherche
    """
    def __init__(self, valeur, sabg=None, sabd=None):
        self.etiquette = valeur
        self.gauche = sabg
        self.droit= sabd

    def est_feuille(self):
        return (self.gauche==None and self.droit==None)

    def __str__(self):
         return str(self.etiquette) + ('-(' + str(self.gauche) + ',' + str(self.droit) + ')' )


def inserer(arbre, n):
    if arbre.etiquette > n:
        if arbre.gauche == None:
            arbre.gauche = ArbreBinaire(n)
        else:
            inserer(arbre.gauche, n)
    else:
        if arbre.droit == None:
            arbre.droit = ArbreBinaire(n)
        else:
            inserer(arbre.droit, n);

def parcoursPrefixe (arbre):
    if arbre!=None:
        print(arbre.etiquette,end=',')
        parcoursPrefixe (arbre.gauche)
        parcoursPrefixe (arbre.droit)

def parcoursSuffixe (arbre):
    if arbre!=None:
        parcoursSuffixe (arbre.gauche)
        parcoursSuffixe (arbre.droit)
        print(arbre.etiquette,end=',')

def parcoursInfixe (arbre):
    if arbre!=None:
        parcoursInfixe (arbre.gauche)
        print(arbre.etiquette,end=',')
        parcoursInfixe (arbre.droit)

def minimum(arbre):
    if arbre.gauche != None:
        return minimum(arbre.filsGauche)
    else:
        return arbre.etiquette

def maximum(arbre):
    if arbre.droit != None:
        return maximum(arbre.droit)
    else:
        return arbre.etiquette

def hauteur(arbre):
    if arbre == None:
        return -1
    else:
        hg = hauteur(arbre.gauche)
        hd = hauteur(arbre.droit)
        if (hg > hd):
            return hg + 1
        else:
            return hd + 1

def nbnoeuds(arbre):
    if (arbre != None):
        return 1 + nbnoeuds(arbre.gauche) + nbnoeuds(arbre.droit)
    else:
        return 0

def etqPresente(arbre, etq):
    if arbre == None:
        return False
    else:
        return arbre.etiquette == etq or etqPresente(arbre.gauche, etq) or etqPresente(arbre.droit, etq)

def nboc(arbre, etq):
    if arbre == None:
        return 0
    else:
        if arbre.etiquette == etq:
            res = 1
        else:
            res = 0
        res = res + nboc(arbre.gauche, etq) + nboc(arbre.droit, etq)
    return res

#Construction de l'ABR
arbre = ArbreBinaire(50)
inserer(arbre, 25)
inserer(arbre, 60)
inserer(arbre, 18)
inserer(arbre, 32)
inserer(arbre, 55)
inserer(arbre, 99)
inserer(arbre, 200)
inserer(arbre, 150)
inserer(arbre, 300)
inserer(arbre, 151)

#Affichage de l'ABR
print("L'ABR est:",arbre)
print("Parcours Prefixe")
parcoursPrefixe(arbre)
print("\nParcours Suffixe")
parcoursSuffixe(arbre)
print("\nParcours Infixe")
parcoursInfixe(arbre)

print("minimum :", hauteur(arbre))
print("maximum :", maximum(arbre))
print("nb noeuds :", nbnoeuds(arbre))
print("hauteur :", hauteur(arbre))
print("Présence étiquette:",etqPresente(arbre, 150))
print("nb occurences :", nboc(arbre, 200))





