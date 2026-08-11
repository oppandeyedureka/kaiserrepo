class Address:
    """Represents a postal address for a customer.

    Stores the street, city, and pincode values and validates that they are non-empty.
    """

    def __init__(self, street, city, pincode):
        """Create a new Address object with street, city, and pincode."""
        self.setStreet(street)
        self.setCity(city)
        self.setPincode(pincode)        
    
    def setStreet(self, street):
        """Validate and set the street field."""
        if len(street.strip())<=0:
            raise ValueError("Invalid street")
        else:
            self.street = street

    def setCity(self, city):
        """Validate and set the city field."""
        if len(city.strip())<=0:
            raise ValueError("Invlaid street")
        else:
            self.city = city

    def setPincode(self,pincode):
        """Validate and set the postal code."""
        if len(pincode.strip())<=0:
            raise ValueError("Invlaid pincode")
        else:
            self.pincode = pincode

    def showAddressDetails(self):
        """Return a tuple of formatted address components."""
        return "Street : ", self.street, " City : ", self.city, " pincode : ", self.pincode