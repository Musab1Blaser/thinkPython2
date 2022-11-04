tn = int(input("Please enter the 1st term: "))
tn1 = int(input("Please enter the 2nd term: "))

# Prints the first 2 terms
print(str(tn) + ", ", end="")
print(str(tn1) + ", ", end="")

# Calculates the next term (tn2) by adding tn1(prev term) and tn(term 2 places before in the series/prev to prev term)
tn2 = tn + tn1

# Prints the new term
print(str(tn2) + ", ", end="")

# shifts the values of tn and tn1 forward along the series by one so that they are the new prev term and prev to prev term
tn = tn1
tn1 = tn2

# Repeats Calculation and Printing 4 more times

tn2 = tn + tn1
print(str(tn2) + ", ", end="")
tn = tn1
tn1 = tn2

tn2 = tn + tn1
print(str(tn2) + ", ", end="")
tn = tn1
tn1 = tn2

tn2 = tn + tn1
print(str(tn2) + ", ", end="")
tn = tn1
tn1 = tn2

tn2 = tn + tn1
print(str(tn2) + ", ", end="")
tn = tn1
tn1 = tn2