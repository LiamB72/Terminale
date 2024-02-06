from fileSansPrio import File


def croisement(f1, f2):
    f3 = File()
    while not f1.estVide() and not f2.estVide():
        pop1 = f1.defiler()

        if pop1 == 1:
            f3.enfiler(pop1)

        elif pop1 == 0:
            pop2 = f2.defiler()

            if pop2 == 2:
                f3.enfiler(pop2)

            elif pop2 == 0:
                f3.enfiler(0)

    if f1.estVide():
        for i in range(len(f2.file)):
            f3.enfiler(f2.defiler())
    elif f2.estVide():
        for i in range(len(f1.file)):
            f3.enfiler(f1.defiler())
    return f3


f1 = File()
f2 = File()
f1.enfiler(0)
f1.enfiler(1)
f1.enfiler(1)
f1.enfiler(0)
f1.enfiler(1)
f2.enfiler(0)
f2.enfiler(2)
f2.enfiler(2)
f2.enfiler(2)
f2.enfiler(0)
f2.enfiler(2)
f2.enfiler(0)
print(f1)
print(f2)
print(croisement(f1, f2))
