from BankingSystem import Account

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
