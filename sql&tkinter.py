import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox
import sqlite3

def Book():
	curItem=tree1.selection()
	name=txtName.get()
	chkinDate=txtCheckin.get()
	chkoutDate=txtCheckout.get()
	
	if name=="" or len(curItem)==0 or chkinDate=="" or chkoutDate=="":
		messagebox.showinfo("Booking","Please enter and select all options to book!")
	else:
	
		conn = sqlite3.connect('hotel.db')	

		sql="insert into Bookings(name,checkin,checkout,type) Values(?,?,?,?)"
		conn.execute(sql,(name,chkinDate,chkoutDate,curItem[0]))
		conn.commit()
		messagebox.showinfo("Booking","Hi "+name+". Your booking for "+curItem[0]+" room from "+chkinDate+" to "+chkoutDate+" is confirmed! See you soon!")
		

def loadTreeData():


	conn = sqlite3.connect('hotel.db')	

	tree1.heading("#0",text="Room Type")

	sql="select * from RoomType"
	conn.row_factory = sqlite3.Row
	rows=conn.execute(sql)

	i=0
	for row in rows:
		
		type=row['type']
		
		tree1.insert("",i,text=type+" Room",iid=type)

		i+=1
		

	tree1.grid(row=3,column=0,columnspan=2)
	
	conn.close()
	
window = tk.Tk() 

window.title("SP Hotel")

label1=ttk.Label(window,text="Name",padding=2)
label1.grid(row=0,column=0,sticky=tk.W)
txtName=StringVar();
entry1=ttk.Entry(window,textvariable=txtName)
entry1.grid(row=0,column=1)


label2=ttk.Label(window,text="Check-in Date(dd/mm/yyyy)",padding=2)
label2.grid(row=1,column=0,sticky=tk.W)
txtCheckin=StringVar();
entry2=ttk.Entry(window,textvariable=txtCheckin)
entry2.grid(row=1,column=1,)

label3=ttk.Label(window,text="Check-out Date(dd/mm/yyyy)",padding=2)
label3.grid(row=2,column=0,sticky=tk.W)
txtCheckout=StringVar();
entry3=ttk.Entry(window,textvariable=txtCheckout)
entry3.grid(row=2,column=1)


tree1=ttk.Treeview(window)
loadTreeData()

button1=ttk.Button(window,text='Book',command=Book)
button1.grid(row=4,column=0,columnspan=2)

window.mainloop() #main loop to wait for events
