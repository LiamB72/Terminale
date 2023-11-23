def verifie(lst:list):
    
    for element in range(len(lst)-1):
        if len(lst) > 1:
            if lst[element] > lst[element+1]:
                print(False)
                return False
    
    print(True)
    return True

verifie([0, 5, 8, 8, 9]) #True
verifie([8, 12, 4]) #False
verifie([-1, 4]) #True
verifie([5]) #True