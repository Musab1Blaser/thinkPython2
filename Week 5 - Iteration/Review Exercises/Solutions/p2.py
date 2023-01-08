def pattern(n):
    t = 1 # keep track of next term to print
    for line in range(n):
        for term in range(2*line + 1): # number of terms increases by 2 for each consecutive line
            print(t, end = " ")
            t = (t + 1) % 10 # if t = 10, then set to 0 (remainder when divided by 10)
        print() # leave a line for formatting

n = int(input())
pattern(n)