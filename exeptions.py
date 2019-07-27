from os import system
file = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical4/q2.txt")
data = file.readlines()

for line in data:
    system("say"+line)
while True:
    try:
        myStudentList=["Jack","Mary","Jerry","Sherry"]
        msg="You have "+str(len(myStudentList))+" students in the list. Which student's name do you want to view? Enter -1 to quit"
        num=int(input(msg))
        if num==-1:
            break
        print(myStudentList[num-1])

    except ValueError as e:
        print("number only")
        print(e)

    except IndexError as e: # usefull in assignment1
        print("number not within range")
        print(e)

        



