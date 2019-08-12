class Student:
    def __init__(self,name,age,diploma):
        self.__name=name
        self.__age=age
        self.__diploma=diploma

def getname(self):
    return self.__name

def getage(self):
    return self.__age

def getdiploma(self):
    return self.__diploma

# def setname(self,name):
#     self.__name=name

# def setage(self,age):
#     self.__age=age
    
# def setdiploma(self,diploma):
#     self.__diploma=diploma

listStudent = []
file=open('/Users/arjunanjana/Desktop/web development/sem2/python p2/precticals/revision prac/input.txt','r')
data=file.readlines()

for line in data:
    line=line.replace('\n','')
    col=line.split(',')
    name=col[0]
    age=col[1]
    diploma=col[2]
    s=Student(name,age,diploma)
    listStudent.append(s)

file.close()

for s in listStudent:
    print(s.getname()+''+s.getdiploma())
