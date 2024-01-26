def fusion(a0: list, a1: list):
    for i in range(len(a1)):
        a0.append(a1.pop())

    for k in range(len(a0)):
        for j in range(len(a0)):

            if a0[k] < a0[j]:
                a0[j], a0[k] = a0[k], a0[j]

    return a0


print(fusion([3, 5], [2, 5]))  # [2, 3, 5, 5]
print(fusion([-2, 4], [-3, 5, 10]))  # [-3, -2, 4, 5, 10]
print(fusion([4], [2, 6]))  # [2, 4, 6]
