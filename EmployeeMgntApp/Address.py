class Address:
    def __init__(self, street, city, pincode):
        if len(street)<=0:
            raise ValueError("Invlaid street")
        else:
            self.street = street

        if len(city)<=0:
            raise ValueError("Invlaid street")
        else:
            self.city = city
            
        if len(pincode)<=0:
            raise ValueError("Invlaid pincode")
        else:
            self.pincode = pincode

    def showAddressDetails(self):
        return "Street : ", self.street, " City : ", self.city, " pincode : ", self.pincode