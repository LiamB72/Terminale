def minimum(tab, d, f) -> int:
    if d == f:
        return tab[d]
    else:
        m = (d + f) // 2
        x = minimum(tab, d, m)
        y = minimum(tab, m + 1, f)
        if x < y:
            return x
        else:
            return y


lst = [23, 12, 4, 56, 35, 57, 3, 11, 6]
print(minimum(lst, 0, len(lst) - 1))
