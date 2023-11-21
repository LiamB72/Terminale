def palindrome(string: str):

    list1 = []
    list2 = []

    for letter in string:

        list1.append(letter)

    for element in list1[::-1]:

        list2.append(element)

    if list1 == list2:

        return True

    return False

print(palindrome("tacocat"))