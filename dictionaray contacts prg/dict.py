from frndata import frn
phonebook = {}#empty dictionary
name = ""
# populate phone book
while name != "Q":
    name = input("plese enter name of person or Q to quit")

    if name == "Q":
        break

    phone = input("plese enter phno of person or Q to quit")
    address = input("pls enter address of person")
    name = name.upper()#to make it case insensitve
    phonebook[name]=frn(phone,address)#refers to the class in the frndata file

#query phone book
name = ""
while name != "Q":
    name = input("plese enter name to find phone number:")

    if name == "Q":
        break

    frienddata = phonebook.get(name.upper())#caseing
    if phone == None:
        print(name+"not in phonebook")
    else:
        print(name+"has phone number"+frienddata.getphone())
        print(name+"address is: "+frienddata.getaddress())
