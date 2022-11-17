import math

def square(character, size):
    extremeLine = (character+" ") * size #extreme lines have size number of characters with spaces after each character
    midLine = character + " " * (2*size - 3) + character #midlines have the same width as extreme lines but only characters at the start and end
    body = (midLine + "\n") * (size-2) #body contains size-2 midlines
    print(extremeLine)
    print(body, end="") #to avoid skipping the extra line
    print(extremeLine)

def rectangle(character, size):
    extremeLine = (character+" ") * size #extreme lines have size number of characters with spaces after each character
    midLine = character + " " * (2*size - 3) + character #midlines have the same width as extreme lines but only characters at the start and end
    body = (midLine + "\n") * (math.ceil(size/2) - 2) #total length is size/2 rounded up, 2 lines reserved for extreme lines
    print(extremeLine)
    print(body, end="") #to avoid skipping the extra line
    print(extremeLine)


character = input()
size = int(input())

square(character, size)
rectangle(character, size)