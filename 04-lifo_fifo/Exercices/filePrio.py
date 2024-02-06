class FilePrioritaire:
    def __init__(self):
        self.file = []

    def __len__(self):
        return len(self.file)

    def __repr__(self):
        return ' '.join([str(i) for i in self.file])

    def enfiler(self, avion):
        self.file.append(avion)

    def defiler(self):
        avion = None
        indicePrioritaire = 0

        if not self.estVide():

            for indice in range(0, len(self.file)):

                if self.file[indice][0] < self.file[indicePrioritaire][0]:
                    indicePrioritaire = indice

            avion = self.file[indicePrioritaire]
            del self.file[indicePrioritaire]

        return avion

    def estVide(self):
        vide = False
        if not self.file:
            vide = True
        return vide
