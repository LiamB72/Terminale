string = input("Input a string :\n")

def checkString(string, character):
    for i in range(len(string)):
        if string[i] == character:
            return True 
        else:
            return False

print(checkString(string, "a"))