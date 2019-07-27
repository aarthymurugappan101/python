from highlowgame import highlowgame 

print("Welcome to High and Low Game")
newgame = highlowgame()

newgame.getrandomnumber()

while(newgame.booleangameended() != True):
    newgame.getuserinput()
    newgame.getresult()