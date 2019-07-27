from practiceq3 import bankaccount

user1 = bankaccount("oliver twist")
user2 = bankaccount("richie rich",100000)

user1.setsavings(1000)
print (user1.displayaccount())
print(user2.displayaccount())