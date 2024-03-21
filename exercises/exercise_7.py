# Your solution to Exercise 7
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operation = input("Enter the operation: ")
if operation == "+":
    print(first_num + second_num)
elif operation == "-":
    print(first_num - second_num)
elif operation == "*":
    print(first_num * second_num)
elif operation == "/":
    if second_num == 0:
        print("Division by 0!")
    else:
        print(first_num / second_num)
elif operation == "pow":
    print(first_num ** second_num)
elif operation == "div":
    print(first_num // second_num)
elif operation == "mod":
    print(first_num % second_num)
