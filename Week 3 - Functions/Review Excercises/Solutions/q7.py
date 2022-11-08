def print_ladder(size):
    nonStep = "* " + "  " * (size - 2) + "*" #note, the space string contains a double space
    gap = (nonStep + "\n") * (size - 2) #each step has a gap of size - 2
    step = "* " * size #each step is a row of asterisks separated by spaces
    ladder = (gap + step + "\n") * size #the ladder starts with a gap and then a step. This pattern repeats size number of times
    print(ladder + gap) #there is one extra gap at the end

size = int(input())
print_ladder(size)