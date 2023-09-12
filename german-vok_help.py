from random import randint

listG=["heraus","bringen","veröffentlichen",
    "erobern",
    "wundersam",
    "ungehorsam",
    "frech",
    "die wildesten Abenteuer",
    "die Sammlung1","der Sammelband2",
    "die Zehn Gebote","die 10 Gebote",
    "das Lagerfeuer",
    "die Weisheit",
    "in grauen Vorzeiten",
    "sie haben sich nicht auserzählt",
    "die Ausgabe","die Auflage",
    "der Einsatz", "das Engagement",
    "die Märchendichter",
    "fest", "halten",
    "bewahren",
    "der Anhang",
    "die bearbeitung",
    "rau",
    "roh",
    "der Zeitspiegel",
    "der drastisch Ausgang1","der drastisch Ausgang2",
    "der Teufel",
    "glatt",
    "kinderverträglich","kinderecht","kindergerecht",
    "schlachten",
    "etwas nach/spielen",
    "das Messer",
    "derweil","währenddessen",
    "ertrinken",
    "sich erhängen",
    "untröstlich",
    "die Trauer",
    "klugerweise",
    "drucken",
    "eine deutchliche Umarbeitung",
    "anzüglich1","anzüglich2",
    "eingezogen sein1","eingezogen sein2",
    "an etw feilen",
    "etw schlüssig gestalten1","etw schlüssig gestalten2",
    "die Anspielung",
    "vermeiden"
    ]

listF=["publier","publier","publier",
    "conquérir",
    "merveilleux",
    "désobéissant",
    "insolent",
    "les aventures les plus folles",
    "le recueil","le recueil",
    "les dix commandements","les 10 commandements",
    "le camp de feu",
    "la sagesse",
    "dans la nuit des temps",
    "elles n'ont pas fini d'être racontées",
    "l'édition", "l'édition",
    "un engagement","un engagement",
    "le conteur",
    "consigner", "conserver",
    "préserver",
    "l'annexe",
    "l'adaptation",
    "rude",
    "brut",
    "le reflet de l'époque",
    "l'issue radicale", "l'issue brutale",
    "le diable",
    "lisse",
    "adapté aux enfants","adapté aux enfants","adapté aux enfants",
    "abattre",
    "imiter qch",
    "le couteau",
    "pendant ce temps","pendant ce temps",
    "se noyer",
    "se pendre",
    "inconsolable",
    "le chagrin",
    "sagement",
    "imprimer",
    "un remaniement significatif",
    "scabreux", "équivoque",
    "faire son entrer", "faire son apparition",
    "peaufiner qch",
    "organiser qch clairement","organiser qch de manière cohérent",
    "l'allusion",
    "éviter"
    ]

class revision():
    
    def __init__(self, G_LIST, F_LIST):
        self.lstG = G_LIST
        self.lstF = F_LIST
        
        self.lenG = len(self.lstG)
        self.lenF = len(self.lstF)

        print(f"German: {self.lenG} words,\nFrench: {self.lenF} words")

        self.z = 0
        self.rand = 0

        self.wordG = self.lstG[self.z]
        self.wordF = self.lstF[self.z]
        
        self.restart = True
        
        self.usedWords = []
        
        while self.restart:
            self.lenghtTraining = int(input("Combien de mots veux tu traduire : "))
            self.lenghtTraining = abs(self.lenghtTraining)

            self.toGerman = input("Veux traduire du français à l'allemand? (Y/N) : ")
            self.toGerman = self.toGerman.lower()
            
            self.toGerman = True if self.toGerman == "y" else False
            
            self.run()
            
            restartInput = input("Restart? (Y/N) : ")

            restartInput = restartInput.lower()
            if restartInput == "y":
                self.restart = True
                self.usedWords.clear()
            else:
                self.restart = False

    def run(self):
        for i in range(self.lenghtTraining):
            self.z = randint(0, self.lenG)
            self.rand = randint(0, 0)

            while not (self.lstG[self.z] in self.usedWords):
                
                print(self.usedWords)
                
                if self.rand == 0:
                    userAnswer = input(f"{self.lstG[self.z]} = ")
                    if userAnswer == self.lstF[self.z]:
                        print("Ya!\n")
                    else:
                        print(f"Nein! das ist {self.lstF[self.z]}\n") 

                elif self.rand == 1 and self.toGerman:
                    userAnswer = input(f"{self.lstF[self.z]} = ")
                    if userAnswer == self.lstG[self.z]:
                        print("Oui!\n")
                    else:
                        print(f"Non! C'est {self.lstG[self.z]}\n")
            
                self.usedWords.append(self.lstG[self.z])
            
            else:
                i -= 1
                
                    
revision(listG, listF)
