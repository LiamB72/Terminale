def fusion(lst_gauche, lst_droit):
    if not lst_gauche:
        return lst_droit
    if not lst_droit:
        return lst_gauche

    if lst_gauche[0] < lst_droit[0]:
        return [lst_gauche[0]] + fusion(lst_gauche[1:], lst_droit)
    else:
        return [lst_droit[0]] + fusion(lst_gauche, lst_droit[1:])


def triFusion(lst):
    if len(lst) == 1:
        return lst
    else:
        m = len(lst) // 2
        lst_gauche = triFusion(lst[:m])
        lst_droit = triFusion(lst[m:])
        print(lst_gauche, lst_droit)
        return fusion(lst_gauche, lst_droit)


lst = [3, 4, 6, 2, 5, 1, 8, 7]
print(triFusion(lst))
