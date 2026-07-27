#create employee class with 3 data members and 2 methods
class Employee:
    #Generic ID Generator
    IDGenerator = 1000
    #constructor
    def __init__(self,empname,salary):
        Employee.IDGenerator = Employee.IDGenerator + 1
        self.empid = Employee.IDGenerator
        self.empname = empname
        self.salary = salary

    #display emp details
    def showempDetails(self):
        return "Emp Id: ", self.empid, " Emp Name: ", self.empname, " Salary: ",self.salary

    #method to be defined in child class
    def showTotalSalary(self):
        pass

#create manager as derived class
class Manager(Employee):
    def __init__(self,empname,salary,perks):
        super().__init__(empname, salary)
        self.perks = perks

    def showTotalSalary(self):
        return self.salary + self.perks

#create Clerk as derived class
class Clerk(Employee):
    def __init__(self,empname,salary,overtime):
        super().__init__(empname,salary)
        self.overtime = overtime

    def showTotalSalary(self):
        return self.salary + self.overtime

#create Salesman as derived class
class Salesman(Employee):
    def __init__(self,empname,salary,commission):
        super().__init__(empname, salary)
        self.commission = commission

    def showTotalSalary(self):
        return self.salary + self.commission

#show polymorphic behavior
def processEmpDetails(empObj):
    0
    print(empObj.showempDetails())
    print(empObj.showTotalSalary())

clrObj = Clerk("Mahesh", 234234.545, 3455345)
processEmpDetails(clrObj)
slsObj = Salesman("Dinesh", 345345.656, 4564556)
processEmpDetails(slsObj)

"""
#Create Objects of Derived classes
mgrObj = Manager("Ganesh", 234234.545, 3455)
print(mgrObj.showempDetails())
print("Total Salary: ", mgrObj.showTotalSalary())

clrObj = Clerk("Mahesh", 234234.545, 3455345)
print(clrObj.showempDetails())
print("Total Salary: ", clrObj.showTotalSalary())

slsObj = Salesman("Dinesh", 234234.545, 4565)
print(slsObj.showempDetails())
print("Total Salary: ", slsObj.showTotalSalary())
"""

mgrObj = Manager("Ganesh", 234234.545, 3455)
processEmpDetails(mgrObj)