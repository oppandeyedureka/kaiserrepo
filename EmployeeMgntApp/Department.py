import os
import pickle


def load_dept_data():
    file_path = os.path.join(os.path.dirname(__file__), "EmpMgntDetails.dat")
    try:
        with open(file_path, "rb") as file:
            return pickle.load(file)
    except (EOFError, FileNotFoundError, AttributeError, ImportError, ModuleNotFoundError, pickle.UnpicklingError):
        print("Error loading department data. Starting with default values.")
        return None


class Department:
    deptcount = 100
    try:
        depts = load_dept_data()
        if not depts:
            deptcount = 100
        else:
            existing_ids = [dept.getDeptId() for dept in depts if hasattr(dept, "getDeptId")]
            deptcount = max([100] + existing_ids)
            print("Dept Count initialized to:", deptcount)
    except Exception:
        deptcount = 100

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