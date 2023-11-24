def indices_maxi(lst:tuple):
    
    maxNb = 0
    nbOccurences = []
    if len(lst) > 1:
        for i in range(len(lst)-1):
            
            if lst[i] > lst[i + 1]:
                
                maxNb = lst[i]
                
        for i in range(len(lst)):
            
            if maxNb == lst[i]:
                
                nbOccurences.append(i)
    elif len(lst) <= 1:
        for i in range(len(lst)):
            maxNb = lst[i]
            nbOccurences = [i]
            print((maxNb, nbOccurences))
            return (maxNb, nbOccurences)
    
    print((maxNb, nbOccurences))
    return (maxNb, nbOccurences)



assert indices_maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8])==(9, [3, 8])
assert indices_maxi([7])==(7, [0])
