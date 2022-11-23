def next_day(year, month, day):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10: #Account for all months with 31 days - except December
        if day == 31: #end of month condition - first day of next month
            month += 1
            day = 1
        else:
            day += 1 #not end of month - next day

    elif month == 2: #Account for February
        if day == 28:
            month += 1
            day = 1
        else:
            day += 1

    elif month == 12: #Account for December
        if day == 31:
            year += 1
            month = 1
            day = 1
        else:
            day += 1

    else:
        if day == 30: #Account for months with 30 days
            month += 1
            day = 1
        else:
            day += 1

    return formatOutput(year, month, day)

def formatOutput(year, month, day):
    y = str(year)

    if month >= 10: #make month into a 2 digit number by adding zero to left if needed
        m = str(month)
    else:
        m = "0" + str(month)

    if day >= 10: #make day into a 2 digit number by adding zero to left if needed
        d = str(day)
    else:
        d = "0" + str(day)

    return (y + "-" + m + "-" + d)

year = int(input())
month = int(input())
day = int(input())

print(next_day(year, month, day))