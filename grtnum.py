def getinput(first):
    first = int(input("Please Enter the First Integer"))
    return first

def getinput2(second):
    second  = int(input("Please Enter The Second Integer"))
    return second

def findmax(first,second):
    if first > second:
        print ("1st Number is bigger")
    elif second > first:
        print ("2nd Number is bigger")
    else:
        print("Both Numbers are equal")
i = getinput('first')
u = getinput2('second')
findmax(i,u)

