# Your solution to Exercise 1

age = input()
if age[1] == ' ':
    a = age[0]
else:
    a = age[0] + age[1]
if len(age) == 4:
    if len(a) == 2:
        print('Alex is the eldest.')
    else:
        print('Tatyana is the eldest.')
else:
    t = age[3] + age[4]
    if int(a) > int(t):
        print('Alex is the eldest.')
    elif int(a) < int(t):
        print('Tatyana is the eldest.')
    else:
        print('Alex and Tatyana are of the same age.')