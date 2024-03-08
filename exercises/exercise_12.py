# Your solution to Exercise 12

num = int(input("Enter a number: "))
first_digit = num // 1000
second_digit = (num // 100) % 10
third_digit = (num // 10) % 10
fourth_digit = num % 10
string = ''
if first_digit % 2 == 0:
    string += '*'
else:
    string += str(first_digit)
if second_digit % 2 == 0:
    string += '*'
else:
    string += str(second_digit)
if third_digit % 2 == 0:
    string += '*'
else:
    string += str(third_digit)
if fourth_digit % 2 == 0:
    string += '*'
else:
    string += str(fourth_digit)
print(string)