from BankingApplication import Account, Savings, Current

try:
    savObj = Savings("Ganesh", 12000, 2000)
    print(savObj.showaccountdetails())
    savObj.withdraw(9000)
    print(savObj.showaccountdetails())
except ValueError:
    print("Invalid value")

try:
    curObj = Current("Mahesh",15000, 5000)
    print(curObj.showaccountdetails())
    curObj.withdraw(20000)
    print(curObj.showaccountdetails())
except ValueError:
    print("Invalid value")

"""
accobj1 = Account(1001, "ABC", 9000.00)
accobj1.showaccountdetails()
accobj1.deposit(5000.00)
accobj1.showaccountdetails()
accobj1.withdraw(2000.00)
accobj1.showaccountdetails()
"""