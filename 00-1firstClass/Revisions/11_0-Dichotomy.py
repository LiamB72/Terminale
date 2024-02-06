import random

def dichotomic_research(element,lst):
    #Creates the variables to be used later.
    start = 0
    end = len(lst)-1
    found = False
    while start <= end and not found:
        #Changes the middle variable each iteration.
        middle = (start + end) // 2
        print(f"Current Middle: {middle}\nCurrent Start : {start}\nCurrent End : {end}")
        #First check : Is the element to found in the middle?
        if element == lst[middle]:
            found = True #If yes then the element is found.
            print(f"Current Middle: {middle}\nCurrent Start : {start}\nCurrent End : {end}")
        else: #If not found, pass to 2nd Check.
            #2nd Check : Is the element passed the middle?
            if element > lst[middle]:
                print(f"Current Middle: {middle}\nCurrent Start : {start}\nCurrent End : {end}")
                start = middle + 1 #If yes, it cuts the start search pass the previous middle 
            else :
                print(f"Current Middle: {middle}\nCurrent Start : {start}\nCurrent End : {end}")
                end = middle - 1 #If not, it cuts the end of the search to before the middle
    #After each iteration, it checks if the element was found.            
    if found: #Is the element found?
        indice = middle #Yes, it target the element and get it's index to be returned.
    else:
        indice = -1 #No, it decrease the index.
    return indice

lst = []
d = {}

for i in range(100):
    lst.append(i)
    
for num in lst:
    d[num] = 1

items = list(d.items())
finalList = [key for key, _ in items]
    
print(finalList)
print(dichotomic_research(37, finalList))