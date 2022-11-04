t1 = int(input("Please enter the 1st term: "))
t2 = int(input("Please enter the 2nd term: "))

# Calculates the next 5 terms
t3 = t2 + t1
t4 = t3 + t2
t5 = t4 + t3
t6 = t5 + t4
t7 = t6 + t5

# Prints each term followed by a comma, uses end to avoid jumping to a new line
print(str(t1) + ", ", end = "")
print(str(t2) + ", ", end = "")
print(str(t3) + ", ", end = "")
print(str(t4) + ", ", end = "")
print(str(t5) + ", ", end = "")
print(str(t6) + ", ", end = "")
print(str(t7))