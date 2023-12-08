def a_doublon(lst:list) -> bool:
    check = 0
    if len(lst) > 1:
        for i in range(len(lst)):
            for j in range(len(lst)):
                if lst[i] == lst[j]:
                    check+=1
            if check > 1:
                return True
            else:
                check = 0
        return False
    else:
        return False

print(a_doublon([]))
print(a_doublon([1]))
print(a_doublon([1, 2, 4, 6, 6]))
print(a_doublon([2, 5, 7, 7, 7, 9]))
print(a_doublon([0, 2, 3]))
