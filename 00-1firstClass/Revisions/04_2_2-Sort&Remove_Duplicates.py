from random import randint
import time

lst = []
d = {}

for _ in range(10000):
    lst.append(randint(1,10000))
    
startTime = time.perf_counter()


#Removing Duplicates :
for num in lst:
    d[num] = 1

items = list(d.items())
finalList = [key for key, _ in items]

lenghtList = len(finalList)

#for every elements in the list
for i in range(lenghtList - 1): 
    
    #Goes through the entire list as it sort itself minus 1
    for j in range(0, lenghtList - i - 1): 
        
        #Seek for the biggest number
        if finalList[j] > finalList[j + 1]: 
            
            #Switch the two without temp variables
            finalList[j], finalList[j + 1] = finalList[j + 1], finalList[j] 
            
    """
    That's a bubble sorting algorithm
    """
            
finalTime = time.perf_counter()

deltaTime = finalTime - startTime
       

print(f"Time taken : {deltaTime:.2f}\n\nList : \n{finalList}")