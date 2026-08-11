class Customer:
    CustIdCount =100
    def __init__(self, customername, address):
        self.customername = customername
        self.customeraddress = address
        self.customerid = self.CustIdCount+1

    def showCustomerDetails(self):
        return "Customer ID : ",self.customerid, "Customer Name : ",self.customername, "Customer Address : ",self.customeraddress.showAddressDetails() 
    