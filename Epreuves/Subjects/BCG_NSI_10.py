def maxliste(lst: list):
    maxElement = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > maxElement:
            maxElement = lst[i]

    return maxElement

print(maxliste([98, 12, 104, 23, 131, 9]))
print(maxliste([-27, 24, -3, 15]))
