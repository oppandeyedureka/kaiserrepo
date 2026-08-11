class Customer:
    """Represents a bank customer with a name, address, and related accounts.

    Tracks a unique customer ID and validates customer details when created.
    """

    CustIdCount =100
    def __init__(self, customername, address):
        """Initialize a Customer with a name and Address object."""
        self.setCustomerName(customername)
        self.setCustomerAddress(address)
        Customer.CustIdCount+=1
        self.customerid = Customer.CustIdCount

    def setCustomerName(self, cname):
        """Validate and store the customer's name."""
        if(len(cname.strip())<=0):
            raise ValueError("Incorrect Name")
        else:
            self.customername = cname

    def getCustomerName(self):
        """Return the customer's name."""
        return self.customername

    def setCustomerAddress(self, addrobj):
        """Validate and set the customer's address object."""
        if addrobj is None:
            raise ValueError("Invalid Address")
        else:
            self.customeraddress = addrobj

    def getCustomerAddress(self):
        """Return the customer's address."""
        return self.customeraddress
    
    def addAccounts(self, accounts):
        """Associate one or more accounts with the customer."""
        self.accounts = accounts

    def getAccounts(self):
        """Return the customer's linked accounts."""
        return self.accounts
    
    def showCustomerDetails(self):
        """Return a tuple containing the customer's details and address."""
        return "Customer ID : ",self.customerid, "Customer Name : ",self.customername, "Customer Address : ",self.customeraddress.showAddressDetails() 

    def getTotalCustomers():
        """Return the total number of customers created."""
        totalcustomers = Customer.CustIdCount-100
        return totalcustomers