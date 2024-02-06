string = input("Make a sentence :\n")

array = []
def separateWords(string):
    words = []
    current_word = ''
    
    for characters in string:
        if characters == ' ':
            if current_word: #checks if the variable isn't empty
                words.append(current_word)
                current_word = ''
        else:
            current_word += characters
               
    # Add the last word if it's not an empty string
    if current_word:
        words.append(current_word)
                
    count = 0

    countList = []

    for word in words:
        for characters in word:
            count += 1
        countList.append(count)
        count = 0
        
    max = countList[0]
    for i in range(1,len(countList)):
        if max < countList[i]:
            max = i

    return words, max

words, max = separateWords(string)

print(f"\n\"{words[max]}\" is the longest word.")
