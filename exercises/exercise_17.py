# Your solution to Exercise 17

ticket_num = input("Enter a ticket number: ")
if int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2]) == int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5]):
    print("Happy")
else:
    print("Ordinary")