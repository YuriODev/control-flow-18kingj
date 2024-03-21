# Your solution to Exercise 10

a_x = float(input("Enter the x-coordinate of point A: "))
a_y = float(input("Enter the y-coordinate of point A: "))
b_x = float(input("Enter the x-coordinate of point B: "))
b_y = float(input("Enter the y-coordinate of point B: "))
c_x = float(input("Enter the x-coordinate of point C: "))
c_y = float(input("Enter the y-coordinate of point C: "))
a = (b_x - a_x)**2 + (b_y - a_y)**2
b = (c_x - b_x)**2 + (c_y - b_y)**2
c = (a_x - c_x)**2 + (a_y - c_y)**2
if a == 0 or b == 0 or c == 0:
    print("No")
elif a + b == c or b + c == a or c + a == b:
    print("Yes")
else:
    print("No")
    