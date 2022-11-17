#outputs the roots of a quadratic equation ax^2 + bx + c = 0
def quadratic_roots(a, b, c):
    determinant = ((b**2) - 4*a*c)**0.5
    smallerRoot = (-b - determinant) / (2*a)
    largerRoot = (-b + determinant) / (2*a)
    print(str(smallerRoot)+", "+str(largerRoot))

a = int(input()) 
b = int(input())
c = int(input())

quadratic_roots(a, b, c)