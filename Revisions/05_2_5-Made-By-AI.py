def find_longest_word(string):
    longest_word = ""
    current_word = ""

    for char in string:
        if char == ' ' or char == ',' or char == ';' or char == '.' or char == '"':
            if len(current_word) > len(longest_word):
                longest_word = current_word
            current_word = ""
        else:
            current_word += char

    # Check the last word in case the string doesn't end with a space
    if len(current_word) > len(longest_word):
        longest_word = current_word

    return longest_word

# Take input from the user
user_input = input("Enter a sentence: ")
longest_word_in_input = find_longest_word(user_input)
print("The longest word in the sentence is:", longest_word_in_input)