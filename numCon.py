def binToDec(str):
    s = len(str)
    power = 0
    decNum = 0

    for i in range(s-1, -1, -1):
        if (str[i] == '1'):
            decNum += (2**power)
        power +=1    
    return decNum

def binToOctal(str):
    decimal = binToDec(str)
    octal = 0
    i = 0
    while decimal > 0:
        octal += (decimal%8)*(10**i)
        i +=1
        decimal //=8
    

    return octal    
# bin = input("Enter the binary number")
# print(binToDec(bin))

bin = input("Enter the Binary numbr to change octal")
print(binToOctal(bin))
