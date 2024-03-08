# Your solution to Exercise 9

num = input("Enter a number: ")
sum = int(num[0]) + int(num[2])
if sum > int(num[1]):
    print(">")
elif sum < int(num[1]):
    print("<")
else:
    print("=")