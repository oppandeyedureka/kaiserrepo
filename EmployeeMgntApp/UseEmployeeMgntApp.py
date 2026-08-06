import os
import pickle

from EmployeeMgntApp import Manager, Clerk, Salesman, load_emp_data
from Department import Department
from Address import Address

def get_data_file(filename):
    return os.path.join(os.path.dirname(__file__), filename)

def LoadExistingDepts():
    depts = load_emp_data()
    return depts if depts else set()

def WriteDeptObject(dept):
    with open(get_data_file("DeptDetails.dat"), "ab") as file:
        #file.write(dept)#Error- TypeError: a bytes-like object is required, not 'Department'
        pickle.dump(dept,file)#Store Object state in File

def ReadDeptObject():
    with open(get_data_file("DeptDetails.dat"), "rb") as file:
        deptobj = pickle.load(file)
    return deptobj

def SaveDepts(depts):
    with open(get_data_file("EmpMgntDetails.dat"), "wb+") as file:
        #file.write(dept)#Error- TypeError: a bytes-like object is required, not 'Department'
        pickle.dump(depts,file)#Store Object state in File

def ReadDepts():
    with open(get_data_file("EmpMgntDetails.dat"), "rb") as file:
        depts = pickle.load(file)
    return depts

try:
    deptobj = Department("Sales","Pune")
    addrobj = Address("ABC","Pune","24234234")
    try:
        empobj1 = Manager("Mgr01", 35234234,deptobj,34535)
        empobj1.setAddress(addrobj)
    except ValueError:
        print("Invalid values in Manager")
    try:
        empobj2 = Clerk("Clr01", 352342,deptobj,34500)
        empobj2.setAddress(addrobj)
    except ValueError:
        print("Invalid values in Clerk")
    emps = set()#Set of Employees 
    emps.add(empobj1)
    emps.add(empobj2)
    deptobj.setEmployees(emps)

    #save multiple departments
    depts = LoadExistingDepts()
    depts.add(deptobj)
    SaveDepts(depts)

    read_depts = ReadDepts()
    print("Read Depts from file:", len(read_depts))
    for dept in read_depts:
        print("Dept ID:", dept.getDeptId())
        employees = dept.getEmployees()
        if employees:
            print("Employees in Dept:", len(employees))
except ValueError:
    print("Invalid values in Dept")
