from fileSansPrio import File

def supressionDernier(fileIn):
    fileOut = File()

    for i in range(len(fileIn)-1):

        fileOut.enfiler(fileIn.defiler())

    return fileOut

f = File()
f.enfiler(5)
f.enfiler(9)
f.enfiler(1)
f.enfiler(3)
print(f)
print(supressionDernier(f))

