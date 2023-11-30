def u(n):
    if n == 0:
        return 3
    else:
        return u(n-1) + 2

print(u(4))