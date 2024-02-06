bit_word = str(input("\nInput your binary message: "))

def convertbit_to_decimals(bit_array):
    
    decimalArray = 0
    bitList = []
    
    for num in bit_array:
        digit = int(num)
        bitList.append(digit)
        
    for i in range(8):
        decimalArray += bitList[i] * (2 ** i)
        
    return decimalArray

print(f"Your message : {bit_word}\nConverted into Decimal : {convertbit_to_decimals(bit_word)}")