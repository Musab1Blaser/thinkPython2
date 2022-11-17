def general_grid(plus, minus, slash, height, width):
    mainLine = ((plus + " ") + (minus + " ") * width) * 2 + plus #a main line is a plus with a space followed by width number of minus+space. This pattern is repeated twice and closed by a final plus
    gap = ((slash + " ") + "  " * (width)) * 2 + slash #a gap is a slash with a space followed by width number of double spaces. This pattern is repeated twice and closed by a final set of slashes
    gaps = (gap + "\n") * height #there is a gap of size height between main lines
    
    #prints the grid with mainlines separated by gaps
    print(mainLine)
    print(gaps, end ="") #gaps had an extra \n so it is removed through the use of end
    print(mainLine)
    print(gaps, end ="")
    print(mainLine)

plus = input()
minus = input()
slash = input()
height = int(input())
width = int(input())

general_grid(plus, minus, slash, height, width)