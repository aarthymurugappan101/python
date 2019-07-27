import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
from tkinter import messagebox

def Hi():
    messagebox.showinfo("Tile","Hi"+" "+entry1Val.get())
    entry1Val.set("")

def select(evt):
	w = evt.widget
	curItem=w.selection()
	print(curItem) #gets the selected iid which is returned as a tuple since can be multiple select for tree view
	print(w.item(curItem[0])) #map of attributes and values related to the selected item
	
def sel():
	selection = "You selected the option " + str(var.get())
	print(selection)    

window = tk.Tk() 
tree1= ttk.Treeview(window)

window.title("My First GUI")
window.geometry("250x500")


label1=ttk.Label(window,text="Name",padding = "10")
label1.grid(row=0,column=0)

var = StringVar()

entry1Val=StringVar()
entry1=ttk.Entry(window,textvariable=entry1Val)
entry1.grid(row=0,column=1)

button1=ttk.Button(window,text='Say Hi',command=Hi)
button1.grid(row=1,column=0,columnspan=2)

tree1.heading("#0",text="Item Listing")
tree1.insert("",0,text="Item 1",iid="0")
tree1.insert("",1,text="Item 2",iid="1")

tree1.grid(row=2,column=1,columnspan=3)
tree1.bind('<ButtonRelease>',select)

R1 = ttk.Radiobutton(window,text="option 1", variable=var,value="1",command=sel)
R1.grid(row=3,column=0)
R2 = ttk.Radiobutton(window, text="Option 2", variable=var,value="2",command=sel)
R2.grid(row=3,column=1)
R3 = ttk.Radiobutton(window, text="Option 3", variable=var,value="3",command=sel)
R3.grid(row=3,column=2)

# assignment convert the console app into a gui app 
# create a movie list use for loop to loop through the movielistand
# then imply it in the treeview
window.mainloop() 