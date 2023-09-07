string = input("Input a string :\n")

a = 0

for i in range(len(string)):
    if string[i] == "e":
        a += 1

print(f"\n\nthe string : '{string}' has {a} \"e\" characters")