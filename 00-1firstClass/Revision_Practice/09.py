tab=[5,9,2,3,6,10,13,45,7]

def lookout(number):
    for i in range(len(tab)):
        if tab[i] == number:
            nIndex = i
            break
        return "Not Found"
    return nIndex

print(f"\nIndex = {lookout(99)}\n")