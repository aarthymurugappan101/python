class user :

    def __init__(self,name,expenditure):
        self._name = name
        self._expenditure = expenditure

    def getname(self):
        return self._name
    
    def setname (self,name):
        self._name = name
    
    def getExpenditure(self):
        return self._expenditure
    
    def setExpenditure(self,expenditure):
        self._expenditure=expenditure
