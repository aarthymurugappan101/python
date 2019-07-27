import sqlite3

def initTable():

	conn = sqlite3.connect('hotel.db')

	#table roomtype
	sql='create table RoomType(type text primary key, description text)'
	conn.execute(sql)
	
	sql="insert into RoomType Values('Single','Single Bed')"
	conn.execute(sql)

	sql="insert into RoomType Values('Double','Twin Bed')"
	conn.execute(sql)
	
	sql="insert into RoomType Values('Family','Max 4 occupancy')"
	conn.execute(sql)
	
	sql="insert into RoomType Values('Suite', 'Max 5 occupancy')"
	conn.execute(sql)
	
	#table bookings
	sql='create table bookings(bookingid integer primary key, name text,checkin text,checkout text,type text)'
	conn.execute(sql)
	
	conn.commit()
	print("Database Tables created!")

	conn.close()
	
def viewBookings():

	conn = sqlite3.connect('hotel.db')

	sql="select * from bookings"
	conn.row_factory = sqlite3.Row
	#cursor.execute(sql)
	#rows=cursor.fetchall()
	rows=conn.execute(sql)

	i=0
	for row in rows:
		#print(row['item'])
		print(str(i+1)+".Name:"+row['name']+",Checkin:"+row['checkin']+",Checkout:"+row['checkout']+",Room:"+row['type']+"\n")
		i+=1
		


	conn.close()
	

print("Welcome to the Hotel admin System")

while True:
	option =input("Choose 1 to create new tables, 2 to view all bookings or Q to quit:")

	if option=="1":
		initTable()
	elif option=="2":
		viewBookings()
	elif option=="Q":
		break
		

