def build_pyramid(max_blocks, c):
    s = ""
    for level in range(abs(max_blocks)): #for each level of the pyramid
        s += " " * (abs(max_blocks) - level - 1) + c * (2*level + 1) + " " * (abs(max_blocks) - level - 1) + "\n" #build the pyramid level - leave space, add characters, leave space
    if (max_blocks < 0):
        s = s[::-1] #flip upside down if height is negative
    print(s)


max_blocks = int(input())
c = input()
build_pyramid(max_blocks, c)