import os
import sys

# Support running as a script or as a package module.
if __package__ is None:
    # running as a script: ensure parent dir is on sys.path so package imports work
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))
    from BankingSystem import Account, Savings, Current, Customer, Address
else:
    # running as a module: use relative imports
    from .Account import Account
    from .Savings import Savings
    from .Current import Current
    from .Customer import Customer
    from .Address import Address

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