import importlib
import os
import pickle

def get_data_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)

class DepartmentUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "Department" and name == "Department":
            return Department
        if module == "Address" and name == "Address":
            return importlib.import_module("EmployeeMgntApp.Address").Address
        if module == "EmployeeMgntApp" and name in {"Employee", "Manager", "Clerk", "Salesman"}:
            return importlib.import_module("EmployeeMgntApp.Employees").__dict__[name]
        if module in {"EmployeeMgntApp.EmployeeMgntApp", "EmployeeMgntApp.Employees"} and name in {"Employee", "Manager", "Clerk", "Salesman"}:
            return importlib.import_module("EmployeeMgntApp.Employees").__dict__[name]
        return super().find_class(module, name)

def load_dept_data():
    try:
        with open(get_data_file("EmpMgntDetails.dat"), "rb+") as file:
            return DepartmentUnpickler(file).load()
    except (EOFError, FileNotFoundError, AttributeError, ImportError, ModuleNotFoundError, pickle.UnpicklingError) as err:
        print("Error loading department data. Starting with default values.", err)
        return None

class Department:
    deptcount = 100
    depts = None

    def __init__(self, deptname, loc):
        self.setDeptName(deptname)
        self.setDeptLoc(loc)
        Department.deptcount += 1
        self.deptid = Department.deptcount

    def setEmployees(self, employees):
        self.Employees = employees

    def getEmployees(self):
        return self.Employees

    def setDeptName(self, deptname):
        if(len(deptname)<=0):
            raise ValueError("Invalid name.")
        else:
            self.deptName = deptname

    def setDeptLoc(self, deptloc):
        if(len(deptloc)<=0):
            raise ValueError("Invalid Location.")
        else:
            self.deptLocation = deptloc
                
    def getDeptName(self):
        return self.deptName

    def getDeptLoc(self):
        return self.deptLocation

    def getDeptId(self):
        return self.deptid

    def getDeptCount(self):
        return Department.deptcount
    
    def showDeptDetails(self):
        return "Dept Id : ", self.getDeptId(), " Dept Name : ", self.getDeptName(), " Dept location:", self.getDeptLoc()

# initialize class-wide department data after class definition
Department.depts = load_dept_data()
if not Department.depts:
    Department.deptcount = 100
else:
    existing_ids = len(Department.depts)
    Department.deptcount = existing_ids + 100
    print("Dept Count initialized to:", Department.deptcount)