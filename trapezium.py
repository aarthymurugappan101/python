class trapezium:
    def __init__(self,base,top,hieght):
        self.base = base
        self.top = top
        self.hieght = hieght

    def getbase(self):
        return self.base
    
    def gettop(self):
        return self.top
    
    def gethieght(self):
        return self.hieght

    def getarea(self):
        return (self.base+self.top)*self.hieght/2

t1 = trapezium(6.0,5.0,4.0)
print ("\nTrapezium class program has started\n")

print ("This Trapezium has base value of :",t1.getbase())
print ("This Trapezium has top value of",t1.gettop())
print ("This Trapezium has hieght value of :",t1.gethieght(),"\n")

print("The area of trapezium is:",t1.getarea(),"\n")

print("The trapezium class has terminated\n")