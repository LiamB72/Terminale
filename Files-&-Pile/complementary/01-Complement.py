def decToBin(n:int):

    p = []
    res = 0

    while True:

        res = n % 2
        n = n // 2
        p.append(res)

        if n == 0:
            break

    return p


print(decToBin(77))
