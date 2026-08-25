class Account:
    """Represents a bank account linked to a customer.

    Stores the account owner, current balance, and a unique account ID.
    Supports deposit and withdrawal operations, with validation for valid amounts.
    """

    AccID =1000 #Select max(accid) from bankingdb.accounts
    def __init__(self, customer, balance):
        """Create a new Account for a customer with an initial balance."""
        self.setCustomer(customer)    
        self.setBalance(balance)
        Account.AccID += 1
        self.accid = Account.AccID
        #Insert into bankingdb.accounts (accid, custid, balance) values (self.accid, self.customer.customerid, self.balance)

    def getAccID(self):
        """Return the numeric account identifier."""
        return self.accid
    
    def setCustomer(self, customer):
        """Assign and validate the customer object for this account."""
        if customer is None:
            raise ValueError("Invalid Customer")
        else:
            self.customer = customer

    def getCustomer(self):
        """Return the customer associated with this account."""
        #select cust.customerid, cust.customername, cust.address 
        # from bankingdb.accounts acc inner join bankingdb.customers cust 
        # on acc.custid = cust.customerid 
        # where acc.accid = self.accid 
        return self.customer
    
    def setBalance(self, amount):
        """Set the account balance, rejecting negative opening balances."""
        if amount<0:
            raise ValueError("Cant penalize bank for account opening.")
        else:
            self.balance = amount

    def getBalance(self):
        """Return the current account balance."""
        return self.balance    

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount<=0:
            raise ValueError("Invalid Amount")
        else:
            self.balance += amount
            #update bankingdb.accounts set balance = self.balance where accid = self.accid
           
    def withdraw(self, amount):
        """Withdraw funds from the account.

        Override this method in subclasses to implement account-specific rules.
        """
        pass
        
    def showaccountdetails(self):
        """Return a tuple containing the account details for display."""
        return "Account Number:", self.accid, " Account Holder: ", self.customer.showCustomerDetails()," Balance: ",self.balance

    def getTotalAccounts():
        """Return the number of accounts created so far."""
        totalAccts = Account.AccID-1000
        return totalAccts