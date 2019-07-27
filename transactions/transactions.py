from user import user
file = open("/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/practical3/transactions/transaction .txt")
lines = file.readlines()

# userlist = []
userdict = {}

for data in lines:
    data = data.replace("\n","")
    cols = data.split(" ")
    name = cols[0]
    expenditure = float(cols[1])

    user1 = user(name,expenditure)

    dup = False #???
    # for eachuser in userlist:
    #     if eachuser.getname()==name:
    #         eachuser.setExpenditure(eachuser.getExpenditure()+expenditure)
    #         dup = True

    # if dup == False:
    #     userlist.append(user1)#???
    val = userdict.get(name)
    if val == None:
        userdict[name] = user1
    else:
        val.setExpenditure(expenditure+val.getExpenditure())
        userdict[name]=val

name = input("please enter the name or -1 to exit")

while name!= '-1':
    # for eachuser in userlist:
    #     if eachuser.getname()==name:
    #         print(name,"spent",eachuser.getExpenditure())
    val = userdict.get(name) #obj stored ind dict
    if val  != None:
        print(name,"spent",val.getExpenditure())
    name = input("please enter the name or -1 to exit: ")
    # dictionary is much faster in searching than looping through a list especially when the data in the list is too long