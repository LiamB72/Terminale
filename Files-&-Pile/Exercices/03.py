from fileSansPrio import File
from pileModule import Pile


def inversionFile(f):
    p = Pile()

    for i in range(len(f)):
        p.empiler(f.defiler())

    for i in range(len(p)):
        f.enfiler(p.depiler())

    return f


f = File()
f.enfiler(5)
f.enfiler(9)
f.enfiler(1)
f.enfiler(3)
print(f)
print(inversionFile(f))
