from .Account import Account

class Savings(Account):
    """Represents a savings account with a minimum balance requirement.

    Inherits from Account and rejects withdrawals that would reduce the balance
    below the configured minimum.
    """

    def __init__(self, customer, balance, minBalance):
        """Create a Savings account enforcing a minimum balance."""
        super().__init__(customer, balance)
        self.setMinBal(minBalance)

    def setMinBal(self, amount):
        """Validate and set the minimum required balance."""
        if amount<=0:
            raise ValueError("Incorrect amount for Min bal")
        else:
            self.minBalance = amount
        
    def withdraw(self, amount):
        """Withdraw money while protecting the minimum balance requirement."""
        if amount<=0:
            raise ValueError("Amount cannot be -ve")
        elif (self.balance-amount)<=self.minBalance:
            raise ValueError("Min Bal error")
        else:
            self.balance -= amount
            #update bankingdb.accounts set balance = self.balance where accid = self.accid
