
def getInput():
    year = int(input("please enter the year"))
    return year


def isLeapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        print("true")
    else:
        print("false")


h=getInput()
isLeapYear(h)
