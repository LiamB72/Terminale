def tri_Selection(tableau):
    N = len(tableau)
    for i in range(0, N - 1):
        indmini = i
        for j in range(i + 1, N):
            if (tableau[j] < tableau[indmini]):
                indmini = j
        if (i != indmini):
            tableau[i], tableau[indmini] = tableau[indmini], tableau[i]