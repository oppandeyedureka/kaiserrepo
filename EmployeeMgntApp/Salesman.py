#create Salesman as derived class
from .Employee import Employee

class Salesman(Employee):
    def __init__(self,empname,salary,deptobj,commission):
        super().__init__(empname,salary,deptobj)
        self.setCommission(commission)
        #print("Sls Object created.")
        
    def setCommission(self, commission):
        if commission<0:
            raise ValueError("commission cannot be -ve")
        else:
            self.commission = commission

    def getCommission(self):
        return self.commission
     
    def showTotalSalary(self):
        return self.getSalary() + self.getCommission()