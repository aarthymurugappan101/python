filename = input("enter the input file name please:")
file =open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical3/p2+t1_data.txt")
data = file.readlines()
length,sum = 0,0
for i in data:
        length+=1
        sum+=int(i)
        avg = sum/length
        
print(filename,"contains",length,"numbers")
print("total sum of all",length,"is",sum) 
print("the average of the numbers is",avg)

