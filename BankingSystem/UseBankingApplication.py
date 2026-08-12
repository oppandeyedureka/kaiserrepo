import os
import sys

if __package__ is None:
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if repo_root not in sys.path:
        sys.path.insert(0, repo_root)

from BankingSystem import Account, Savings, Current, Customer, Address

try:
    addrObj = Address("Hingewadi","Pune","42342342")
    custObj = Customer("Ganesh",addrObj)

    accounts = set()
    try:
        savObj = Savings(custObj, 12000, 2000)
        savObj.withdraw(9000)
        accounts.add(savObj)
        savObj.setCustomer(custObj)
    except ValueError:
        print("Invalid value")

    try:
        curObj = Current(custObj,15000, 5000)
        curObj.withdraw(20000)
        accounts.add(curObj)
        curObj.setCustomer(custObj)
    except ValueError:
        print("Invalid value")

    custObj.addAccounts(accounts)
    for acc in custObj.getAccounts():
        print(acc.showaccountdetails())

    print("Total Customers : ", Customer.getTotalCustomers())
    print("Total Accounts : ", Account.getTotalAccounts())
except ValueError as err:
    print("Got an error",err)