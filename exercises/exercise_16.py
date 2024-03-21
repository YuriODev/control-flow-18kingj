# Your solution to Exercise 16

leap = False
day = int(input("Enter a day: "))
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))
if year % 4 == 0:
    leap = True
if month == 1 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day > 1:
        day -= 1
    else:
        day = 30
        if month == 1:
            day = 31
            month = 12
            year -= 1
        else:
            month -= 1
elif month == 3:
    if leap:
        if day > 1:
            day -= 1
        else:
            day = 29
            month -= 1
    else:
        if day > 1:
            day -= 1
        else:
            day = 28
            month -= 1
else:
    if day > 1:
        day -= 1
    else:
        day = 31
        month -= 1
if len(str(day)) == 1:
    day = '0' + str(day)
if len(str(month)) == 1:
    month = '0' + str(month)
print(day, month, year, sep='.')