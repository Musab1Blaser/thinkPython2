def name_of_firm(name_1, name_2):
    #alphabetically smaller name (regardless of case) becomes the first name
    if name_1.lower() < name_2.lower():
        firstName = name_1
        secondName = name_2
    else:
        firstName = name_2
        secondName = name_1

    name = firstName + ", " + secondName + " & Associates"

    #double underline if first name is smaller, otherwise single underline
    if len(firstName) <= len(secondName):
        name += "\n" + ("=" * len(name))
    else:
        name += "\n" + ("-" * len(name))

    return name

name_1 = input()
name_2 = input()

print(name_of_firm(name_1, name_2))
     