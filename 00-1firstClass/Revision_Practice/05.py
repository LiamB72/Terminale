import time

"""class calculusBoard():
    def __init__(self):
        while True:
            
            self.a = int(input("First number: "))
            self.b = int(input("Second number: "))
            
            self.print_choices()
            
            choice = str(input("You chose : "))
            
            self.print_choices()
            
            if choice != "q":
                choice = int(choice)
                if (choice > 0 and choice < 5):
                    self.operation()
                    
                else:
                    print("Invalid choice!")
            else:
                break
                
    def print_choices(self):
        print("\n<<------------------>>",
                  "\n \"1\" : Addition ",
                  "\n \"2\" : Substraction",
                  "\n \"3\" : Multiplication",
                  "\n \"4\" : division",
                  "\n \"q\" : Quit",
                  "\n<<------------------>>\n"
                  )   
            
    def operations(self):
        if (choice == 1):
            res = self.a + self.b
            print(f"{self.a} + {self.b} = {res}\n\n<<------------------>>\n")
            
        elif (choice == 2):
            res = self.a - self.b
            print(f"{self.a} - {self.b} = {res}\n\n<<------------------>>\n")
            
        elif (choice == 3):
            res = self.a * self.b
            print(f"{self.a} x {self.b} = {res}\n\n<<------------------>>\n")
            
        elif (choice == 4):
            res = self.a / self.b
            print(f"{self.a} / {self.b} = {res}\n\n<<------------------>>\n")
            
calculusBoard()"""

def printChoix():
    print("\n<<----------------->>",
      "\n1 : Addition",
      "\n2 : Soustraction",
      "\n3 : Multiplication",
      "\n4 : Division",
      "\nq : Quitter",
      "\n<<----------------->>\n")

printChoix()
choice = str(input("Ton choix : "))

a = int(input("1ère Valeur = "))
b = int(input("2ème Valeur = "))

while choice != 'q':
    
    choice = int(choice)
    
    if choice > 0 and choice < 5:
        
        print("\n<<----------------->>")
        if choice == 1:
            print(f"\nResultat : {a} + {b} = {a+b}")
        
        elif choice == 2:
            print(f"\nResultat : {a} - {b} = {a-b}")
            
        elif choice == 3:
            print(f"\nResultat : {a} * {b} = {a*b}")
            
        elif choice == 4:
            if b != 0:
                print(f"\nResultat : {a} / {b} = {a/b}")
            else:
                print("Impossible")
        
        time.sleep(1)
        
    printChoix()
    choice = str(input("Ton choix : ")) 
    if choice == "q":
        break       
    
    a = int(input("1ère Valeur = "))
    b = int(input("2ème Valeur = "))
    
if choice == "q":
    print("\nBye!")