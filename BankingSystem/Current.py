from .Account import Account

class Current(Account):
    """Represents a current account with an overdraft facility.

    Inherits from Account and allows withdrawals up to the sum of balance
    and overdraft limit.
    """

    def __init__(self, customer, balance, overdraft):
        """Create a Current account with an overdraft limit."""
        super().__init__(customer, balance)
        self.setOverdraft(overdraft)

    def setOverdraft(self, amount):
        """Validate and set the overdraft limit."""
        if amount<=0:
            raise ValueError("Invaid amount for Overdraft.")
        else:
            self.overdraft = amount

    def withdraw(self, amount):
        """Withdraw money allowing overdraft up to the account limit."""
        if amount<=0:
            raise ValueError("Invalid amount")
        elif amount>(self.balance + self.overdraft):
            raise ValueError("Going above Overdraft")
        else:
            self.balance -= amount
