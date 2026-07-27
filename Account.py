class Account:
    def __init__(self, accid, holdername, balance):
        self.accid = accid
        self.holdername = holdername    
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
           
    def withdraw(self, amount):
        self.balance -= amount
        
    def showaccountdetails(self):
        print(f"Account Number: {self.accid}, Account Holder: {self.holdername}, Balance: {self.balance}")   

accobj1 = Account(1001, "ABC", 10000.00)
accobj1.showaccountdetails()
accobj1.deposit(5000.00)
accobj1.showaccountdetails()
accobj1.withdraw(2000.00)
accobj1.showaccountdetails()