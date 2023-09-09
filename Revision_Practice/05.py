class calculusBoard():
    def __init__(self):
        while True:
            
            self.a = int(input("First number: "))
            self.b = int(input("Second number: "))
            
            self.print_choices()
            
            choice = str(input("You chose : "))
            
            self.print_choices()
            
            if (choice == "1" or choice == "2" or choice == "3" or choice == "4" or choice == "q"):
                if choice == "1":
                    self.add()
                    pass
                if choice == "2":
                    self.substract()
                    pass
                if choice == "3":
                    self.multiply()
                    pass
                if choice == "4":
                    self.divide()
                    pass
                if choice == "q":
                    print("Goodbye!\n\n<<------------------>>\n")
                    break
            else:
                print("Invalid choice!")     
                
    def print_choices(self):
        print("\n<<------------------>>",
                  "\n \"1\" : Addition ",
                  "\n \"2\" : Substraction",
                  "\n \"3\" : Multiplication",
                  "\n \"4\" : division",
                  "\n \"q\" : Quit",
                  "\n<<------------------>>\n"
                  )   
            
    def add(self):
        res = self.a + self.b
        print(f"{self.a} + {self.b} = {res}\n\n<<------------------>>\n")
        
    def subtract(self):
        res = self.a - self.b
        print(f"{self.a} - {self.b} = {res}\n\n<<------------------>>\n")
        
    def multiply(self):
        res = self.a * self.b
        print(f"{self.a} x {self.b} = {res}\n\n<<------------------>>\n")
        
    def divide(self):
        res = self.a / self.b
        print(f"{self.a} / {self.b} = {res}\n\n<<------------------>>\n")
            
calculusBoard()