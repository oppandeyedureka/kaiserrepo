from EmployeeMgntApp import *
from Department import Department
from Address import Address

#using nested try blocks
try:
    dname = input("Enter department name : ")
    dloc =  input("Enter department location : ")
    deptobj = Department(dname, dloc)
    try:
        street = input("Enter street : ")
        city =  input("Enter city : ")
        pincode =  input("Enter pincode : ")
        #Department details are compulsory
        empobj = Manager("Ganesh",123123, deptobj, 23424)
        addrobj = Address(street, city, pincode)
        empobj.setAddress(addrobj)#optional value
        print(empobj.getAddress())
        print(empobj.showempDetails())
        print(empobj.getDeptDetails())
    except ValueError:
        print("Manager object failed.")
    except NameError:
        print("Address object failed")

    try:
        clrobj = Clerk("Mahesh",2323344, deptobj, 345345)
        print(clrobj.showempDetails())
        print(clrobj.getDeptDetails())
        clrobj.setAddress(addrobj)
        print(clrobj.getAddress())
    except ValueError:
        print("Clerk Object failed")
except ValueError:
    print("Invalid details for resource creation")

"""
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


try:
    empname = input("Enter valid emp name:")
    empsalary = float(input("Enter valid emp salary:"))
    mgrperks = float(input("Enter valid perks for manager:"))
    mgrObj = Manager(empname, empsalary, mgrperks)
    processEmpDetails(mgrObj)
except ValueError:
    print("Invalid value.")

"""