import mysql.connector
import math
mydb = mysql.connector.connect(host="localhost",user = "root", password = "root", database = "movie")
mycursor = mydb.cursor()

class Cinema:
    def show_seats(self,row,seats):
        global tickets_booked
        tickets_booked = 0
        print("Cinema:")
        for i in range(row+1):
            for j in range(seats+1):
                if i == 0:
                    if i == j == 0:
                        print(" ",end = " ")
                        continue
                    else:
                        print(j, end= " ")
                else:
                    if i ==1 and j == 0:
                        print("")
                    else:
                        count = 1
                        print(i , end= " ")
                        while(True):
                            if count <= seats:
                                seatno = int(str(i)+str(count))
                                sql = 'select * from customer where seat_no = %s'
                                val = (seatno,)
                                mycursor.execute(sql,val)
                                res = mycursor.fetchone()
                                if res:
                                    print("B", end=" ")
                                    tickets_booked = tickets_booked + 1
                                else:
                                    print("S", end=" ")
                                count = count + 1
                            else:
                                print("")
                                break
                        break

    def buy_ticket(self, row, seats):
        brow = int(input("Enter row:"))
        bcol = int(input("Enter col:"))
        if brow <= row and bcol <= seats:
            seat_no = int(str(brow) + str(bcol))
            ticket_price = 0
            res = row * seats
            if res <= 60:
                ticket_price = 10
            else:
                division = row / 2
                res1 = math.floor(division)
                if brow <= res1:
                    ticket_price = 10
                else:
                    ticket_price = 8

            print("Ticket price :", ticket_price)

            ans = input("You want to Book (yes/no):")
            ch = ans.lower()
            if ch == "yes":
                name = input("Enter Name:")
                gender = input("Enter Gender:")
                age = int(input("Enter Age:"))
                phone = input("Enter phone number:")
                sql = "insert into customer(Name,Gender,Age,phone_num,seat_no,ticket_price) values (%s,%s,%s,%s,%s,%s);"
                val = (name, gender, age, phone, seat_no, ticket_price)
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.execute('select * from customer where Name = name')
                res = mycursor.fetchall()
                if res:
                    print("Booked Successfully")
                else:
                    print("ERROR:Try again")
            else:
                print("Booking Cancelled.")
        else:
            print("Seat not available")

    def show_statistics(self,row,seats):
        global total_income
        total_income = 0
        print("Number of purchased tickets:",tickets_booked)
        divisor = row * seats
        per_of_tickets_booked = (tickets_booked /divisor)*100
        print("Percentage:",str(round(per_of_tickets_booked,2))+"%")
        seat_data = int(str(row) + str(seats))
        sql = "select sum(ticket_price) from customer where seat_no <= %s"
        val = (seat_data,)
        mycursor.execute(sql,val)
        res = mycursor.fetchone()
        for price in res:
            print("Current Income:","$"+str(price))
        res = row * seats
        if res <= 60:
            total_income = 10 * seats * row
        else:
            res = row / 2
            division_row = math.floor(res)
            premium_tickets_price = 10 * seats * division_row  # formula = price * number of columns * number of rows
            normal_tickets_rows = row - division_row
            normal_tickets_price = 8 * seats * normal_tickets_rows
            total_income = premium_tickets_price + normal_tickets_price
        print("Total Income:","$"+str(total_income))


    def show_booked_ticket(self):
        brow = int(input("Enter row:"))
        bcol = int(input("Enter col:"))
        sno = int(str(brow) + str(bcol))
        sql = "select Name,Gender,Age,ticket_price,phone_num from customer where seat_no = %s;"
        val = (sno,)
        mycursor.execute(sql, val)
        res = mycursor.fetchone()
        if res:
            print("Name:", res[0])
            print("Gender:", res[1])
            print("Age:", res[2])
            print("Ticket Price:", str(res[3]) + "$")
            print("Phone No:", res[4])
        else:
            print("Ticket for respective seat is not booked.")