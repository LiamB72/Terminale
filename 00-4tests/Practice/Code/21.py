def multiplication(n1, n2):
    
    res = 0
    
    if n2 > 0:
        
        for _ in range(n2):
            res += n1
            
    elif n2 < 0:
        
        for _ in range(n2, 0):
            res -= n1
        
    return res

print(multiplication(3,5))
print(multiplication(-4,-8))
print(multiplication(-2,6))
print(multiplication(-2,0))