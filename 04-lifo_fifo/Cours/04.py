class Pile:
    def __init__(self):
        self.pile = []

    def __len__(self):
        return len(self.pile)

    def __repr__(self):
        return ' '.join([str(i) for i in self.pile])

    def empiler(self, element):
        self.pile.append(element)

    def depiler(self):
        return self.pile.pop()

    def estVide(self):
        if len(self.pile) == 0:
            return True
        return False

    def sommet(self):
        if not self.estVide():
            return self.pile[-1]
        

def catcutter(a, b, symbol):
    
    if symbol == '+':
        
        res = a + b
        
    elif symbol == '-':
        
        res = a - b
    
    elif symbol == '*':
        
        res = a * b
    
    elif symbol == '/':
        
        if a != 0:
            res = a / b
            
        else:
            
            print("error; can't divide by zero.")
        
    return res


def polonaise(liste:list):
    
    p = Pile()
    
    for element in liste:
    
        if element in  ['+', '-', '*', '/']:
        
            b = p.depiler()
            a = p.depiler()
            r = catcutter(a, b, element)
            p.empiler(r)
        
        else:
            p.empiler(element)
    
    return p.depiler()

print(polonaise([2,3,'-']))
print(polonaise([2,3,'*']))
print(polonaise([2,3,'+',4,'*']))
print(polonaise([4,3,2,'*','/']))