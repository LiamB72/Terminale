a = int(input("#1: "))
b = int(input("#2: "))
c = int(input("#3: "))

def trianglePossible(a, b, c):
    return True if (a + b > c) and (a + c > b) and (b + c > a) else False

def triangleType(a, b, c):
    if trianglePossible(a, b, c):
        if (a == c) or(b == c) or(a == b):
            return 'Isocele'

        if (a == b == c):
            return 'equilateral'
        
        else :
            return 'Whatever'
    return 'Triangle is not possible'

"""def triangleType(a,b,c):
    if trianglePossible(a,b,c):
        return 'Isocele' if (a == c) or (b == c) or (a == b) else ('equilateral' if (a == b == c) else 'Whatever')
    else:
        return 'Triangle is not possible'"""
print(triangleType(a, b, c))