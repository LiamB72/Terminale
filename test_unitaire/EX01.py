def moyenne(lst):

    lenght = len(lst)
    sum = 0
    for i in range(lenght):
        sum += lst[i]

    moy = sum/lenght

    return round(moy,2)


assert moyenne([1]) == 1
assert moyenne([1,2,3,4,5,6,7]) == 4
assert moyenne([1,2]) == 1.5
