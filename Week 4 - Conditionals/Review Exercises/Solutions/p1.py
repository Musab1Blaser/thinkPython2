def largest_of_three(a, b, c):
    if a >= b and a >= c: #is a the largest
        return a
    elif b >= a and b >= c: #is b the largest
        return b
    elif c >= a and c >= b: #is c the largest
        return c


a = int(input())
b = int(input())
c = int(input())

print("largest:",largest_of_three(a, b, c))