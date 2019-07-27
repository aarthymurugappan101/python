class Student:
# defining class
    def  __init__(self,name, adminNumber, course, group):
        # __makes it private or invisible__
        # try: 
        #     x=int(group)
            self.__name = name
            self.__adminNumber = adminNumber
            self.__course = course
            if group>0:
                self.__group = group
            else:
                self.__group=1
    # def setName(self,name):
    #     self.__name=name
        
    def setgroup(self,group):
        if group>0:
            self.__group=group
        else:
            self.__group=1
    def getgroup(self):
        return self.__group
    def getname (self):
        return self.__name
    def setname (self,name):
        self.__name=name
    
        # except exeption as err:
        #     print ("group should be a number! for student"+name)
    def printdetails(self):
        print("hi my name is"+ self.__name+"and i am taking course"+self.__course)
# DEFINE THE OBJECT
stlist=[]
st1 = Student("john","p7337022","NVMP",1)
st2 = Student("aarthy","p7664911","NVMP",2)
st3 = Student("jan","p9772977","NVMP",1)

stlist.append(st1)
stlist.append(st2)
stlist.append(st3)

for s in stlist:
    s.printdetails()

grp=int(input("enter the group of students you want to find"))
for s in stlist:
    if s.getgroup() == grp:
        print(s.getname())
        # print (s.__name)