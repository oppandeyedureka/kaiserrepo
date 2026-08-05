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
        
    def setCommission(self, commission):
        if commission<0:
            raise ValueError("commission cannot be -ve")
        else:
            self.commission = commission

    def getCommission(self):
        return self.commission
     
    def showTotalSalary(self):
        return self.getSalary() + self.getCommission()
