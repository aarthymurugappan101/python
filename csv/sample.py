filename = input("enter the input file name please: ")

output = input("enter the input file name please: ")

file = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical3/csv/sample.csv")
outputfile = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical3/csv/sample1.csv","w")

lines = file.readlines()

for a in lines:
    cols = a.split(",")

    for e in cols:
        e = e.replace("\n","")
        outputfile.write("["+e+"]")
        print(e)
    outputfile.write("\n")

file.close()
outputfile.close()