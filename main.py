from cinema import Cinema

row = int(input('Enter the number of rows:\n'))
seats = int(input("Enter the number of seats in each row:\n"))
while(True):
    ch = input("1. Show the seats\n2. Buy a ticket\n3. Statistics\n4. Show booked Tickets User Info\n0. Exit\n")
    if ch == "1":
        obj = Cinema()
        obj.show_seats(row,seats)

    if ch == "2":
        obj = Cinema()
        obj.buy_ticket(row,seats)

    if ch == "3":
        obj = Cinema()
        obj.show_statistics(row,seats)

    if ch == "4":
        obj = Cinema()
        obj.show_booked_ticket()

    if ch == "0":
        break



