def multiplication(a0, a1):
    res = 0
    if a1 > 0:
        for i in range(a1):
            res += a0
    elif a1 < 0:
        for i in range(a1, 0):
            res -= a0
    return res

print(multiplication(3, 5))
print(multiplication(-4, -8))
print(multiplication(-2, 6))
print(multiplication(-2, 0))
