import sqlite3

def createTable():
    conn=sqlite3.connect("hotel.db")
    sql = "Create Table Booking(bookingId integer primary key, name text, checkin text, checkout text, type text)"
    conn.execute(sql)
    sql = "insert into booking(bookingId,name, checkin , checkout, type) values(?,?,?,?)"
    conn.execute(sql(1,"John","01/01/2018","03/01/2018","Single"))
    conn.execute(sql(2,"Ted","05/01/2018","10/01/2018","Double"))
    conn.commit()
    conn.close()

    def selectTable():
        conn.sqlite3.connect("hotel.db")

        conn.row_factory=sqlite3.Row

        sql="Select * from booking"
        rows=conn.execute(sql)

        count = 1
        for row in rows:
            name = row['name']
            checkin=row['checkin']
            checkout=row['checkout']
            type = row['type']
            print(str(count)+'.Name:'+name+',checkin:'+checkin+',checkout:'+checkout+',room:'+type)
            count+=1
            conn.close()
userinput=""
while userinput!="Q":
    userinput=input("choose 1 to create new tables, 2 to view all the bookings")
    if userinput == "1":
        createTable()
        print("database tables created")
    elif userinput =="2":
        selectTable()