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

    def setSalary(self, salary):
        if salary<=0:
            raise ValueError("Incorrect Salary value")
        else:
            self.salary = salary

    #display emp details
    def showempDetails(self):
        return "Emp Id: ", self.empid, " Emp Name: ", self.empname, " Salary: ",self.salary

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

    def showTotalSalary(self):
        return self.salary + self.perks

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
    def showTotalSalary(self):
        return self.salary + self.overtime

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
        
    def showTotalSalary(self):
        return self.salary + self.commission


