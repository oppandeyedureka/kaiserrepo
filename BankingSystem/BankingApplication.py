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
        return f"Account Number: {self.accid}, Account Holder: {self.customer.showCustomerDetails()}, Balance: {self.balance}" 

class Savings(Account):

    def __init__(self, customer, balance, minBalance):
        super().__init__(customer, balance)
        self.setMinBal(minBalance)

    def setMinBal(self, amount):
        if amount<=0:
            raise ValueError("Incorrect amount for Min bal")
        else:
            self.minBalance = amount
        
    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Amount cannot be -ve")
        elif (self.balance-amount)<=self.minBalance:
            raise ValueError("Min Bal error")
        else:
            self.balance -= amount
    
class Current(Account):
    def __init__(self, customer, balance, overdraft):
        super().__init__(customer, balance)
        self.setOverdraft(overdraft)

    def setOverdraft(self, amount):
        if amount<=0:
            raise ValueError("Invaid amount for Overdraft.")
        else:
            self.overdraft = amount

    def withdraw(self, amount):
        if amount<=0:
            raise ValueError("Invalid amount")
        elif amount>(self.balance + self.overdraft):
            raise ValueError("Going above Overdraft")
        else:
            self.balance -= amount

class Customer:
    CustIdCount =100
    def __init__(self, customername, address):
        self.customername = customername
        self.customeraddress = address
        self.customerid = self.CustIdCount+1

    def showCustomerDetails(self):
        return "Customer ID : ",self.customerid, "Customer Name : ",self.customername, "Customer Address : ",self.customeraddress.showAddressDetails() 
    