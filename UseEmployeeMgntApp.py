from EmployeeMgntApp import *

#show polymorphic behavior
def processEmpDetails(empObj):
    print(type(empObj))
    print(empObj.showempDetails())
    print(empObj.showTotalSalary())

try:
    clrObj = Clerk("Mahesh", 234234.545, 3455345)
    processEmpDetails(clrObj)
except ValueError:
    print("Provided details are incorrect.")

try:
    slsObj = Salesman("Dinesh", 345345.656, 4564556)
    slsObj.setCommission(12000)
    slsObj.showTotalSalary()
    slsObj.setEmpName("Dinesh Rathore")
    slsObj.setSalary(1200000)
    processEmpDetails(slsObj)
except ValueError:
    print("Provided details are incorrect.")

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

try:
    empname = input("Enter valid emp name:")
    empsalary = float(input("Enter valid emp salary:"))
    mgrperks = float(input("Enter valid perks for manager:"))
    mgrObj = Manager(empname, empsalary, mgrperks)
    processEmpDetails(mgrObj)
except ValueError:
    print("Invalid value.")