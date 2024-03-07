# Your solution to Exercise 3

num = int(input('Enter a number: '))
output = ''
if num == 0:
    output = 'Green'
elif num < 11:
    if num % 2 == 0:
        output = 'Black'
    else:
        output = 'Red'
elif num < 19:
    if num % 2 == 0:
        output = 'Red'
    else:
        output = 'Black'
elif num < 29:
    if num % 2 == 0:
        output = 'Black'
    else:
        output = 'Red'
elif num < 37:
    if num % 2 == 0:
        output = 'Red'
    else:
        output = 'Black'
else:
    print('The bet will not play!')
print(output)