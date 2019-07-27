import random

class highlowgame:
    def __init__ (self,randomnumber=-1,guess=-1):#??
        self.randomnumber = randomnumber
        self.guess = guess

    def getrandomnumber(self):
        self.randomnumber = random.randint(0,99)
        # print(self.randomnumber)

    def getuserinput(self):
        self.guess = int(input("Enter your guess: "))
    
    def getresult(self):
        if self.randomnumber > self.guess:
            print(self.guess,"is lower than the secret number")
        elif self.randomnumber < self.guess:
            print(self.guess,"is higher than the secret number")
        else:
            print("you are correct")
    
    def booleangameended(self):
        if self.randomnumber == self.guess:
            return True