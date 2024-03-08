# Your solution to Exercise 13
yes = False
num = input("Enter a number: ")
if num[0] != num[3] and num[1] != num[2] and num[0] != num[1] and num[1] != num[2] and num[2] != num[3]:
    yes = True
print(yes)