from random import randint
from fileSansPrio import File

def extractionPaire(fileIn):
    fileOut = File()

    for element in fileIn.file:

        tempStr = str(element)
        if tempStr[-1] in ["0", "2", "4", "6", "8"]:

            fileOut.enfiler(element)

    return fileOut

f = File()
for n in range(0, 20):
    f.enfiler(randint(10, 50))

print(f)
print(extractionPaire(f))
