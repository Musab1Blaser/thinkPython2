def potato(verses):
    poem = ""
    #fill poem with consecutive verses
    for verse in range(verses):
        poem += generateVerse(verse) + "\n" #verse 0 = 1 potato, 2 potato... 4!\n5 potato... MORE!
    return poem

# first line of each verse contains 3*"(num) potato, " followed by "(num)!"
# second line of each verse contains 3*"(num) potato, " followed by "MORE!"
def generateVerse(verse):
    s = ""
    for i in range(1, 4):
        s += str(7*verse + i) + " potato, "
    s += str(7*verse + 4) + "!\n"
    for i in range(5, 8):
        s += str(7*verse + i) + " potato, "
    s += "MORE!"
    return s

verses = int(input())
print(potato(verses))