def to_binary(val):
    binary_rep = ""
    while val > 0:
        lst_digit = val % 2 # extract last binary digit
        binary_rep = str(lst_digit) + binary_rep # store digit at the beginning of current binary string 
        val = val//2 # shift binary string one position to the right
    return binary_rep

val = int(input())
print(to_binary(val))