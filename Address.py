class Address:
    def __init__(self, street, city, pincode):
        self.street = street
        self.city = city
        self.pincode = pincode

    def showAddressDetails(self):
        return "Street : ", self.street, " City : ", self.city, " pincode : ", self.pincode