class Department:
    deptcount = 100

    def __init__(self, deptname, loc):
        self.setDeptName(deptname)
        self.setDeptLoc(loc)
        Department.deptcount += 1
        self.deptid = Department.deptcount

    def setDeptName(self, deptname):
        if(len(deptname)<=0):
            raise ValueError("Invalid name.")
        else:
            self.deptName = self.deptName

    def setDeptLoc(self, deptloc):
        if(len(deptloc)<=0):
            raise ValueError("Invalid Location.")
        else:
            self.deptLocation = deptloc
                
    def showDeptDetails(self):
        return "Dept Id : ", self.deptid, " Dept Name : ", self.deptName, " Dept location:", self.deptLocation
    