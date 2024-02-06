class temperatureConversion():
    def __init__(self, choice, temperature):
        self.temp = temperature
        
        choice.lower()
        
        if (choice == "c"):
            self.convert_to_celsius()
        elif (choice == "f"):
            self.convert_to_fahrenheit()
    
    def convert_to_fahrenheit(self):
        fahenreit = (self.temp * 1.8) + 32
        return fahenreit
    
    def convert_to_celsius(self):
        degre = (self.temp - 32)/1.8
        return degre

print(temperatureConversion("C", 64).convert_to_celsius())

"""def conversionTemp(F):
    degre = (F - 32)/1.8
    fahenreit = (degre * 1.8) + 32
    
    print(f"{degre}, {fahenreit}")
    
conversionTemp(108)"""