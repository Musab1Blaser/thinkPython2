def makes_triangle(a, b, c): 
    if a < b + c and b < a + c and c < a + b: # Check that each side is smaller than the sum of the other two
        return True
    else:
        return False

a = int(input())
b = int(input())
c = int(input())

print(makes_triangle(a, b, c))