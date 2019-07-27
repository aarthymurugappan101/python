# def getInput():
#         rank= int(input("plesse enter your rank"))
#         return rank

# def printPrize(rank):
#         if rank == 1:
#                 prize = "1000"
#         elif rank == 2:
#                 prize = "800"
#         elif rank == 3:
#                 prize = "700"
#         elif rank ==4:
#                 prize = "300"
#         elif rank == 5:
#                 prize = "300"
#         else:
#                 prize = "20"    
        
#         print("your prize money is"+str(prize))

# r=getInput()
# printPrize(r)

def getInput():
        farenhiet = float(input("please enter the farenhiet value"))
        return farenhiet
def convertCelcius(farenhiet):
        celcius = 5/9*(farenhiet-32)
        print(round(celcius,2))
i=getInput()
convertCelcius(i)