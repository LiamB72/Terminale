def triangle(height):
    for h in range(1,height + 1):
        for lenght in range(1, h + 1):
            print("*", end='')
        print()
    
triangle(5)