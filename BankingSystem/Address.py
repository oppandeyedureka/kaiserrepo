class Address:
    def __init__(self, street, city, pincode):
        self.setStreet(street)
        self.setCity(city)
        self.setPincode(pincode)        
        
    def setStreet(self, street):
        if len(street)<=0:
            raise ValueError("Invlaid street")
        else:
            self.street = street

    def setCity(self, city):
        if len(city)<=0:
            raise ValueError("Invlaid street")
        else:
            self.city = city

    def setPincode(self,pincode):
        if len(pincode)<=0:
            raise ValueError("Invlaid pincode")
        else:
            self.pincode = pincode

    def showAddressDetails(self):
        return "Street : ", self.street, " City : ", self.city, " pincode : ", self.pincode