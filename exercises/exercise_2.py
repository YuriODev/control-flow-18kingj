# Your solution to Exercise 2

age = int(input('Enter your age: '))
if age < 2:
    print('You are an infant.')
elif age < 13:
    print('You are a child.')
elif age < 20:
    print('You are a teenager.')
else:
    print('You are an adult.')