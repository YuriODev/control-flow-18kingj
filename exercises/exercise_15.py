# Your solution to Exercise 15

leap = False
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
if year % 4 == 0:
    leap = True
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day < 31:
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
elif month == 2:
    if leap:
        if day < 29:
            day += 1
        else:
            day = 1
            month += 1
    else:
        if day < 28:
            day += 1
        else:
            day = 1
            month += 1
else:
    if day < 30:
        day += 1
    else:
        day = 1
        month += 1
print(day, month, year, sep='.')