class Customer:
    """Represents a bank customer with a name, address, and related accounts.

    Tracks a unique customer ID and validates customer details when created.
    """

    CustIdCount =100 #selct max(customerid) from bankingdb.customers
    def __init__(self, customername, address):
        """Initialize a Customer with a name and Address object."""
        self.setCustomerName(customername)
        self.setCustomerAddress(address)
        Customer.CustIdCount+=1
        self.customerid = Customer.CustIdCount
        #Insert into bankingdb.customers (customerid, customername, street, city, pincode) values (self.customerid, self.customername, self.address.city, self.address.street, self.address.pincode)

    def setCustomerName(self, cname):
        """Validate and store the customer's name."""
        if(len(cname.strip())<=0):
            raise ValueError("Incorrect Name")
        else:
            self.customername = cname
            #update bankingdb.customers set customername = self.customername where customerid = self.customerid

    def getCustomerName(self):
        """Return the customer's name."""
        #selcectquery = 'select customername from bankingdb.customers where customerid = %s'
        #values = (self.custid)
        #cursor.execute(selcectquery, values)
        return self.customername

    def setCustomerAddress(self, addrobj):
        """Validate and set the customer's address object."""
        if addrobj is None:
            raise ValueError("Invalid Address")
        else:
            self.customeraddress = addrobj
            #update bankingdb.customers(street, city, pincode) 
            #values(this.addrobj.street, this.addrobj.city, this. addrobj.pincode)

    def getCustomerAddress(self):
        """Return the customer's address."""
        return self.customeraddress
    
    def addAccounts(self, accounts):
        """Associate one or more accounts with the customer."""
        self.accounts = accounts

    def getAccounts(self):
        """Return the customer's linked accounts."""
        #select acc.accid, acc.balance, acc.overdraft, acc.minbalance 
        #from bankingdb.accounts as acc where acc.custid = custid
        return self.accounts
    
    def showCustomerDetails(self):
        """Return a tuple containing the customer's details and address."""
        #Select custid, custname, street, city, pincode from bankingdb.customers where custis = self.custid
        return "Customer ID : ",self.customerid, "Customer Name : ",self.customername, "Customer Address : ",self.customeraddress.showAddressDetails() 

    def getTotalCustomers():
        """Return the total number of customers created."""
        totalcustomers = Customer.CustIdCount-100
        #Select count(*) from bankingdb.customers
        return totalcustomers