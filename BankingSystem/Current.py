from BankingSystem import Account

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
