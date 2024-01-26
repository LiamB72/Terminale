def multiplication(a0: int, a1: int):
    res = 0
    if a0 > 0:
        for i in range(a0):
            res += a1
    elif a0 < 0:
        for i in range(a0, 0):
            res -= a1

    return res

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
