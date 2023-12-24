def u(n):
    if n == 0:
        return 5
    else:
        return 2*u(n-1)

print(u(4))
