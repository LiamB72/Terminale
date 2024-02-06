def occ(word):
    
    d = {}

    word = word.lower()
    
    for letter in range(len(word)):
        if word[letter] in d:
            d[word[letter]] = d[word[letter]] + 1
            
        else:
            d[word[letter]] = 1
            
    return d

print(occ("Torture"))