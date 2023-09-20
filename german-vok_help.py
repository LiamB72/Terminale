from random import randint

wordsToLearn = {
    "die Märchen" : {
        "lstG" : ["das Märchen", "die wundersame Geschichte", "die Erzählung (1)", "die Erzählung (2)", "eine Geschichte erzählen",
                  "das Kulturgut", "das Volk", "volkstümlich", "die Volkserzählung", "das Volksmärchen",
                  "der Zeitspiegel", "zeitgemäß", "ein zeitloses Motiv haben", "die Wirklichkeit wider", "der Realität entsprechen",
                  "der Zauber", "die Zauberwelt", "etw. zaubern", "das Vorlesen", "jm vor/lesen", "jm ein Märchen vor/lesen",
                  "der Ursprung ursprünglich", "früher", "heute", "heutzutage", "damals", "der Mund", "der Volksmund",
                  "etw. mündlich überliefern", "überliefert sein", "für Kinder gedacht sein", "für Kinder geeignet sein",
                  "der Erwachsene", "sich an Erwachsene richten", "das Ende", "gut enden", "die Moral",
                  "ein Märchen ist eine moralische Geschichte", "ein Märchen bringt eine ethische Lehre", "es hat einen pädagogischen Zweck",
                  "Grimms Märchen sind Erziehungsbücher", "die Botschaft", "eine Botschaft vermitteln", "die Wahrnehmung etw. wahr/nehmen",
                  "die Persönlichkeitsentwicklung", "die Emanzipation", "das Wert", "die Tugend", "die bestrafen", "die Bestrafung",
                  "jn bestrafen", "die Belohnung", "jn vor einer Gefahr retten", "jm das Leben retten", "die Veröffentlichung",
                  "veröffentlichen", "sammeln", "das Sammeln", "der Sammelband", "die Sammlung"],
                     
        "lstF" : ["le conte", "l'histoire merveilleuse", "le récit", "l'histoire", "raconter une histoire",
                  "un élément du patrimoine culturel", "le peuple populaire", "traditionnel", "le récit populaire",
                  "le reflet de l'époque", "conforme à l'époque, contemporain", "avoir un thème intemporel", "refléter la réalité", "correspondre à la réalité",
                  "le sort", "le monde enchanté", "faire apparaître qch (comme) par magie", "la lecture", "faire la lecture à qn", "lire un conte à qn",
                  "l'origine au début", "autrefois", "aujourd'hui", "de nos jours", "à l'époque", "la bouche", "le langage populaire",
                  "transmettre qch oralement", "être transmis de génération en génération", "être pensé pour les enfants", "être adapté pour les enfants",
                  "l'adulte", "s'adresser aux adultes", "la fin", "bien finir", "la morale", "un conte est une histoire morale", "un conte apporte un enseignement éthique",
                  "il a un objectif pédagogique", "les contes de Grimm sont des livres d'éducation", "le message", "transmettre un message", "la perception, percevoir, comprendre qch",
                  "la perception, percevoir, comprendre qch", "le développement personnel", "l'émancipation", "la valeur", "la vertu", "la punition", "sanction",
                  "punir qn, sanctionner qn", "la récompense", "sauver qn d'un danger", "sauver la vie de qn", "la publication", "publier", "collecter", "la collecte", "le recueil", "la collection"]
    },
    "die Angst" : {
        "lstG" :  ["die Angst", "etw. aus Angst machen", "Angst bekommen", "vor jm/etw. Angst haben", 
                   "sich vor jm/etw. ängstigen", "um jn Angst haben", "jm Angst machen", 
                   "beängstigend sein", "der Schreck (1)", "der Schreck (2)", 
                   "jm einen Schreck ein/jagen", "jn erschrecken", "erschrecken", 
                   "erschreckend sein", "schrecklich sein", "die Furcht", "Furcht vor jm haben", 
                   "sich vor jm/etw. fürchten", "etw. fürchten", "furchtbar sein", "das Gruseln", 
                   "sich gruseln", "die Gruselgeschichte", "der Gruselfilm", "gruselig", "schauern",
                   "vor Entsetzen erschauern", "jn erschauern lassen", "der Schauerroman"],
        
        "lstF" : ["la peur", "faire qch par peur", "prendre peur", "avoir peur de qn", 
                  "avoir peur de qch", "avoir peur pour qn", "faire peur à qn", "être effrayant", 
                  "la peur", "l'effroi", "faire peur à qn", "faire peur à qn", "avoir peur", 
                  "être effrayant", "être affreux", "la crainte", "avoir peur de qn", 
                  "avoir peur de qch", "craindre qch", "terrible", "le frisson", "avoir le frisson",
                  "le récit d'épouvante", "le film d'épouvante", 
                  "épouvantable", "frissonner", "frissonner d'épouvante", "donner le frisson à qn",
                  "le roman d'épouvante"]
    },
    "HVE" : {
        "lstG": ["der Held", "die Heldin", "das Vorbild vorbildlich", "exemplarisch", "jm als Vorbild dienen", 
		        "sich jn zum Vorbild nehmen", "das Mädchen nimmt sich ihre Mutter zum Vorbild", "eine Rolle nach/spielen", 
		        "die Eigenschaft", "gute und schlechte Eigenschaften haben", "das Wert", "frech sein", "gehorsam", "ungehorsam", 
		        "vorsichtig", "unvorsichtig", "die Weisheit weise sein", "die Klugheit klug sein", "lebensklug sein", "schlau", 
		        "die Macht mächtig sein", "die Bosheit boshaft", "böse", "die Güte gut sein", "die Menschlichkeit menschlich sein", 
		        "die Schönheit", "schön sein", "das Abenteuer", "abenteuerlustig sein", "der Mut", "mutig sein", "der Fleiß", "fleißig sein",
		        "die Treue", "treu sein"],

        "lstF": ["le héros", "la héroïne", "le modèle exemplaire", "le modèle exemplaire", "servir de modèle à qn", 
	    	    "prendre qn pour modèle", "la fille prend modèle sur sa mère", "reproduire, rejouer un rôle après qn", 
	    	    "le trait de caractère", "avoir des qualités et des défauts", "la valeur", "être insolent", "obéissant", "désobéissant", 
	    	    "prudent", "imprudent", "la sagesse", "le bon sens", "avoir du bon sens", "astucieux, malin", "le pouvoir être puissant", 
	    	    "la méchanceté", "méchant", "être bon", "l'humanité être humain", "la beauté", "être beau", "l'aventure", 
	    	    "avoir le goût de l'aventure", "le courage", "courageux", "le zèle", "être travailleur", "la fidélité", "être fidèle"]
    }
}

class revision():
    
    def __init__(self):
        
        self.restart = True
        
        while self.restart:
            
            self.define_lists()

            print(f"\n\nGerman: {self.lenG} words,\nFrench: {self.lenF} words")

            if self.userInput == "r":
                self.define_variables()
            
            print("\n\n<<-------------------->>\n\n")
            
            if self.userInput == "r" :
                self.run_revision()
            if self.userInput == "t" :
                self.run_translate()
            
            restartInput = input("Restart? (Y/N) : ")

            restartInput = restartInput.lower()
            if restartInput == "y":
                self.restart = True
                if self.userInput == "r":
                    self.usedWords.clear()
            else:
                self.restart = False

    def define_lists(self):
        self.userInput = input("\nRevison (R) / translation (T) : ")
        self.userInput = self.userInput.lower()

        theme = input("\nMärchen Themed (M)\nAngst Themed (A)\nHeld - Vorbild - Eigenschaften Themed (HVE)\nChoice: ")
        theme = theme.lower()

        if theme == "m":
            self.lstG = wordsToLearn["die Märchen"]["lstG"]
            self.lstF = wordsToLearn["die Märchen"]["lstF"]
        if theme == "a":
            self.lstG = wordsToLearn["die Angst"]["lstG"]
            self.lstF = wordsToLearn["die Angst"]["lstF"]
        if theme == "hve":
            self.lstG = wordsToLearn["HVE"]["lstG"]
            self.lstF = wordsToLearn["HVE"]["lstF"]
            
        self.lenG = len(self.lstG)
        self.lenF = len(self.lstF)

    def define_variables(self):
        self.z = 0
        self.rand = 0
        
        self.wordG = self.lstG[self.z]
        self.wordF = self.lstF[self.z]
        
        self.usedWords = []
        
        self.lenghtTraining = int(input("\nCombien de mots veux tu traduire : "))
        self.lenghtTraining = abs(self.lenghtTraining)

        self.toGerman = input("\nVeux traduire du français à l'allemand? (Y/N) : ")
        self.toGerman = self.toGerman.lower()
        
        self.toGerman = True if self.toGerman == "y" else False

    def run_revision(self):
        if self.lenghtTraining <= self.lenG:
            a = 0
            while a < self.lenghtTraining:
                a += 1
                self.z = randint(0, self.lenG-1)
                if self.toGerman:
                    self.rand = randint(0, 4)
                else:
                    self.rand = 0
                    
                #print(a, self.z)

                if (self.lstG[self.z] in self.usedWords):
                    self.lenghtTraining += 1

                else: 
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
            for _ in range(self.lenghtTraining):
                self.z = randint(0, self.lenG-1)
                if self.toGerman:
                    self.rand = randint(0, 4)
                else:
                    self.rand = 0
                    
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

    def run_translate(self):
        
        for i in range(self.lenG):
            print(f"\nGerman no.{i+1:2}: \"{self.lstG[i]}\"", end="")
        
        userTranslate = input("\n\nGerman word : ")
        notFound = 0
        for i in range(self.lenG):
            
            if userTranslate == self.lstG[i]:
                notFound -= notFound
                print(f"\n{userTranslate} = {self.lstF[i]}\n")
                break
            
            notFound += 1
        if notFound > 1:
            print("\nWord not found")
    

revision()
