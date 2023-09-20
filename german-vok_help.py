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
    }
    
}


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


class translationT_To_F():
    
    def __init__(self, lstG, lstF):
        
        self.lstG = lstG
        self.lstF = lstF

        self.lenG = len(self.lstG)
        self.lenF = len(self.lstF)
        
        self.restart = True
        
        while self.restart:
            self.run()
            
            restartInput = input("Restart? (Y/N) : ")

            restartInput = restartInput.lower()
            if restartInput == "y":
                self.restart = True
                
            else:
                self.restart = False
        
    def run(self):
        
        userTranslate = input("German word : ")
        notFound = 0
        for i in range(self.lenG):
            
            if userTranslate == self.lstG[i]:
                notFound -= notFound
                print(f"\n{userTranslate} = {self.lstF[i]}\n")
                break
            
            notFound += 1
        if notFound > 1:
            print("Word not found")
    

while True:
    userInput = input("Revison or translatinon? R/T : ")
    userInput = userInput.lower()
    
    theme = input("Märchen Theme? or Angst Theme? M/A : ")
    theme = theme.lower()
    
    if theme == "m":
        listG = wordsToLearn["die Märchen"]["lstG"]
        listF = wordsToLearn["die Märchen"]["lstF"]
    if theme == "a":
        listG = wordsToLearn["die Angst"]["lstG"]
        listF = wordsToLearn["die Angst"]["lstF"]
        
    print(f"Theme Chosen : {theme},\nlstG : \n{listG}\n\nlstF : \n{listF}\n\n\n")
    
    
    if userInput == "r":
        revision(listG, listF)

    elif userInput == "t":
        translationT_To_F(listG, listF)
        pass

    else:
        print(f"\nGot: {userInput} \n\nExpected: \"R\" or \"T\"\n")
