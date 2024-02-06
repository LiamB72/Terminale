def medianList(list):
    total = 0
    lenght = len(list)
    for _ in range(lenght):
        total += list[_]
    return (f"The median of {list} is {total / lenght}")

print(medianList([13,5,2,5,1,7]))