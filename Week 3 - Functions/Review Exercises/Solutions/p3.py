def breakdown(num4):
    num4 = int(num4)

    #find digit value at each position
    thousands = getDigit(num4, 4)
    hundreds = getDigit(num4, 3)
    tens = getDigit(num4, 2)
    units = getDigit(num4, 1)

    #formatted output
    print("Thousands:", thousands)
    print("Hundreds:", hundreds)
    print("Tens:", tens)
    print("Units:", units)
 
#finds the value at a specific digit position counting from right to left
def getDigit(num4, digitPos):
    num4 = num4 % (10**digitPos)
    digitVal = num4 // (10**(digitPos-1))
    return digitVal

num4 = input()
breakdown(num4)


