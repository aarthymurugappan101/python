#  create an init function to set length and width 
#  write code to get area()
#  func to get perimeter() ret peri of rect
class rectangle:
    def  __init__(self,length,width):
        self.length = length
        self.width = width

    def getarea(self):
        return self.length*self.width
    
    def getperimeter(self):
        return 2*self.length+2*self.width

newRectangle = rectangle(10,5)
print("area: ",newRectangle.getarea())
print("perimeter: ",newRectangle.getperimeter())
