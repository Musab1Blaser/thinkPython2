import math

#calculates area using pi * (r^2)
def circle_area(r):
    area = math.pi * (r ** 2)
    return round(area, 2) #send back answer rounded to 2 decimal places

r = int(input("Please enter the radius of your circle: "))
print(circle_area(r))