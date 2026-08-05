class Department:
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
    
    def showDeptDetails(self):
        return "Dept Id : ", self.getDeptId(), " Dept Name : ", self.getDeptName(), " Dept location:", self.getDeptLoc()
    