string = input("Write something:\n")

new_string = ""

for characters in string:
    new_string += characters + "*"

new_string = new_string[:-1]
    
print(new_string)