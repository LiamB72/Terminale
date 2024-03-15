a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'],
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'],
     'H':['','']}

def taille(abr, lettre):
    if lettre == "":
        return 0
    return 1 + taille(abr, abr[lettre][0]) + taille(abr, abr[lettre][1])
    
    
    
print(taille(a, 'F'))
print(taille(a, 'B'))
print(taille(a, 'I'))
