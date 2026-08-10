import importlib
import os
import pickle

def get_data_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)


class EmployeeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module in {"EmployeeMgntApp.Employees", "EmployeeMgntApp", "EmployeeMgntApp.EmployeeMgntApp"} and name in {"Employee", "Manager", "Clerk", "Salesman"}:
            return getattr(importlib.import_module("EmployeeMgntApp.Employees"), name)
        if module in {"Department", "EmployeeMgntApp.Department"} and name == "Department":
            return importlib.import_module("EmployeeMgntApp.Department").Department
        if module in {"Address", "EmployeeMgntApp.Address"} and name == "Address":
            return importlib.import_module("EmployeeMgntApp.Address").Address
        return super().find_class(module, name)


def load_emp_data():
    try:
        with open(get_data_file("EmpMgntDetails.dat"), "rb") as file:
            return EmployeeUnpickler(file).load()
    except (EOFError, FileNotFoundError, AttributeError, ImportError, ModuleNotFoundError, pickle.UnpicklingError) as err:
        print("File loading error in Emp", err)
        return None


#create employee class with 3 data members and 2 methods
class Employee:
    #Generic ID Generator
    IDGenerator = 1000
   #constructor
    def __init__(self,empname,salary, deptobj):
        Employee.IDGenerator = Employee.IDGenerator + 1
        self.empid = Employee.IDGenerator
        self.setEmpName(empname)
        self.setSalary(salary)

        #Add association of Department with Employee
        #self.department = deptobj
        self.setDepartment(deptobj)
        

    def getDeptDetails(self):
        return self.department.showDeptDetails()
    
    #centralize validation logic
    def setEmpName(self, empname):
    #raise exception based on condition
        if len(empname)<=0:
            raise ValueError("Emp Name cannot be empty")
        else:
            self.empname = empname

    def setDepartment(self, deptobj):
        self.department = deptobj

    def setAddress(self, addrobj):
        if addrobj is None:
            raise ValueError("Invalid address")
        else:
            self.Address = addrobj

    def getAddress(self):
        return self.Address.showAddressDetails()
    
    def setSalary(self, salary):
        if salary<=0:
            raise ValueError("Incorrect Salary value")
        else:
            self.salary = salary

    def getSalary(self):
        return self.salary
    
    def getEmpID(self):
        return self.empid

    def getEmpName(self):
        return self.empname
    
    #display emp details
    def showempDetails(self):
        return "Emp Id: ", self.getEmpID(), " Emp Name: ", self.getEmpName(), " Salary: ",self.getSalary()

    #method to be defined in child class
    def showTotalSalary(self):
        pass


#create manager as derived class
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

#create Clerk as derived class
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

#create Salesman as derived class
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


depts = load_emp_data()
if not depts:
    Employee.IDGenerator = 1000
else:
    existing_ids = []
    for dept in depts:
        employees = dept.getEmployees()
        if employees:
            existing_ids.extend(emp.getEmpID() for emp in employees)
    Employee.IDGenerator = max([1000] + existing_ids)
