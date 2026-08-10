import os
import sys

if __package__ is None:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from EmployeeMgntApp.Department import Department
from EmployeeMgntApp import Manager
from EmployeeMgntApp.Address import Address
import pickle

def WriteDeptObject(depts):
    with open("EmpMgntDetails.dat", "ab") as file:
        #file.write(dept)#Error- TypeError: a bytes-like object is required, not 'Department'
        pickle.dump(depts,file)#Store Object state in File

def ReadDeptObject():
    with open("EmpMgntDetails.dat", "rb") as file:
        depts = pickle.load(file)
        print("Dept Count initialized to:", deptobj.getDeptId())
    return depts

deptobj = Department("Sales","Pune")
addrobj = Address("ABC","Pune","24234234")
empobj1 = Manager("Mgr01", 35234234,deptobj,34535)
empobj1.setAddress(addrobj)

emps = set()#Set of Employees 
emps.add(empobj1)
deptobj.setEmployees(emps)

depts = set()
depts.add(deptobj)

WriteDeptObject(depts)
ReadDeptObject()