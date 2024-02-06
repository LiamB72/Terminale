gender = input("\nH/F : ")
height = int(input("\nHeight (in cm) : "))

def perfectWeight(gender, height):

    gender = gender.lower()

    if gender == "h":
        perfect_weight = height - 100 - ((height - 150) /4)
    elif gender == "f":
        perfect_weight = height - 100 - ((height - 150) /2.5)
        
    return perfect_weight
    
print(f"{perfectWeight(gender, height):.2f} kg")