def is_right(a, b, c):
    a2 = a**2
    b2 = b**2
    c2 = c**2
    if (a2 == b2 + c2) or (b2 == a2 + c2) or (c2 == a2 + b2): #Check if the square of any side equals the sum of the squares of the other 2 sides
        return True
    else:
        return False


a = int(input())
b = int(input())
c = int(input())

print(is_right(a, b, c))