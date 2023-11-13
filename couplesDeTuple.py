# Liam BERGE TG1 | Temps Pris: 29 mins
# Mathématique Expertes

n = int(input("n = "))

class Couples:
    
    def __init__(self, n):
        
        self.nInt = n
        self.divided = []
        self.couple = []
        
    def seekDivided(self):
        self.divided.clear()
        for i in range(1,self.nInt):
            
            res = self.nInt % i
            
            if res == 0:
                
                self.divided.append((i, n//i))
    
    def removeDoubles(self):
        
        rList = []
        rList.extend(self.divided[::-1])
        
        for i in range(len(self.divided)-1):
            
            self.couple.append(rList[i])           
            j = 0
            
            while j <= len(self.couple)-1:
                
                if self.couple[j][0] == rList[i+1][1]:
                    
                    self.couple.pop(j)
                
                j += 1
            
        self.couple.append(rList[len(rList)-1])
        self.couple.reverse()

        if self.couple[len(self.couple)-1][0] == self.couple[len(self.couple)-1][1]:
            
            self.couple.pop()
        
    def __repr__(self):
        self.seekDivided()
        self.removeDoubles()
        return f"{self.couple}"
                
c = Couples(n)
print(c)

#Log(O²) = exponentiellement plus complexe (temps qu'il prend à executer) en fonction de n
