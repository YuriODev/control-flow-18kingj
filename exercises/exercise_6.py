# Your solution to Exercise 6

a_x = float(input("Enter the x-coordinate of point A: "))
a_y = float(input("Enter the y-coordinate of point A: "))
b_x = float(input("Enter the x-coordinate of point B: "))
b_y = float(input("Enter the y-coordinate of point B: "))
line_a = a_x ** 2 + a_y ** 2
line_b = b_x ** 2 + b_y ** 2
if line_a > line_b:
    print("A is further from the origin.")
elif line_a < line_b:
    print("B is further from the origin.")
else:
    print("A and B are at the same distance from the origin.")
