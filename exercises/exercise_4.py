# Your solution to Exercise 4

grade = int(input('Enter your grade: '))
if 4 > grade > 0:
    print('initial level')
elif 7 > grade:
    print('average level')
elif 10 > grade:
    print('sufficient level')
elif 13 > grade:
    print('high level')
else:
    print('level is absent')
    