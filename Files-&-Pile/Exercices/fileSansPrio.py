class File:
    def __init__(self):
        self.file = []

    def __len__(self):
        return len(self.file)

    def __repr__(self):
        return ' '.join([str(i) for i in self.file])

    def enfiler(self, avion):
        self.file.append(avion)

    def defiler(self):
        return self.file.pop(0)

    def estVide(self):
        vide=False
        if not self.file:
            vide=True
        return vide 
