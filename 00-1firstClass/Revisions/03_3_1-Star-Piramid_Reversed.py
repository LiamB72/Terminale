def triangle(height):
    for h in range(height, 0, -1):
        for lenght in range(h, 0, -1):
            print("*", end='')
        print()
    
triangle(5)