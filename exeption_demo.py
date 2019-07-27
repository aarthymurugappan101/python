try:
    x = float(input("enter a number"))
    x1 = float(input("enter a another number"))
    z = 10/0
    print(x)
    print(y)

except ValueError as e : #this comes first if you want to use 2 or more exeption
     print(e)

except ZeroDivisionError as e:
     print("it is zero division error")

except Exception as e: # any kind of error will b captured the most genral exeption must be at the bottom
    print(e)

print("run")