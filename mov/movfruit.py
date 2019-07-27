#Write a Python script to first read the contents of both the files and 
#Place the data in two corresponding list. Print out the size and contents of both the list.
file = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical3/mov/friuts.txt")
linef = file.readlines()

file = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical3/mov/mov.txt")
linem = file.readlines()


print (len(linef))
print (linef,end="\n")


print (len(linem))
print(linem,end="")

file.close()