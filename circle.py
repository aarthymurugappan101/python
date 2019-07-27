import math
class circle:
    def __init__(self,radius):
        self.radius = radius

    def getcircumfrance(self):
        return 2*math.pi*self.radius
    
    def getarea(self):
        return math.pi*math.pow(self.radius,2)

    def enlargecircle(self):
        self.radius*=3
    
    def shrinkcircle(self):
        self.radius/=2
        
    

