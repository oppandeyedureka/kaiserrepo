from BankingSystem import Account, Savings, Current, Customer, Address

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

