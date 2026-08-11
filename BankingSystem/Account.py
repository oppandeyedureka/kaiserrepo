class Account:
    AccID =1000
    def __init__(self, customer, balance):
        self.setCustomer(customer)    
        self.setBalance(balance)
        Account.AccID += 1
        self.accid = Account.AccID

    def setCustomer(self, customer):
        self.customer = customer
        
    def setBalance(self, amount):
        if amount<0:
            raise ValueError("Cant penalize bank for account opening.")
        else:
            self.balance = amount
        
    def deposit(self, amount):
        if amount<=0:
            raise ValueError("Invalid Amount")
        else:
            self.balance += amount
           
    def withdraw(self, amount):
        pass
        
    def showaccountdetails(self):
        return f"Account Number: {self.accid}, Account Holder: {self.customer}, Balance: {self.balance}" 
