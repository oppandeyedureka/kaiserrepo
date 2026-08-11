#create Clerk as derived class
from .Employee import Employee

class Clerk(Employee):
    def __init__(self,empname,salary,deptobj,overtime):
        super().__init__(empname,salary,deptobj)
        self.setOvertime(overtime)
        
    def setOvertime(self, overtime):
        if overtime<0:
            raise ValueError("Overtime cannot be -ve")
        else:
            self.overtime = overtime

    def getOvertime(self):
        return self.overtime
    
    def showTotalSalary(self):
        return self.getSalary() + self.getOvertime()
