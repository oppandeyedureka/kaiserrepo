#create manager as derived class
from .Employee import Employee

class Manager(Employee):
    def __init__(self,empname,salary,deptobj,perks):
        super().__init__(empname, salary, deptobj)
        self.setPerks(perks)

    def setPerks(self, perks):
        if perks<0:
            raise ValueError("Perks cannot be -ve")
        else:
            self.perks = perks

    def getPerks(self):
        return self.perks
    
    def showTotalSalary(self):
        return self.getSalary() + self.getPerks()
