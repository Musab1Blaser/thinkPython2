def countCurrency(amount):
    #outputs the amount of notes of each denomination while updating amount to what is left to accomodate
    amount = notesOf(5000, amount)
    amount = notesOf(1000, amount)
    amount = notesOf(500, amount)
    amount = notesOf(100, amount)
    amount = notesOf(20, amount)
    amount = notesOf(10, amount)
    amount = notesOf(1, amount)

def notesOf(denomination, amount):
    print(denomination, ":", amount//denomination) #outputs the maximum number of notes possible with current denomination
    return amount % denomination #returns the remaining amount

amount = int(input())
countCurrency(amount)