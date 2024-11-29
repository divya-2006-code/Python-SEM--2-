#1.
class Library:
     def __init__(self,library_name,library_address):
         self.library_name = library_name
         self.library_address = library_address
     def displayLibraryDetails(self):
        print(f"Library Name:{self.library_name}\nLibrary Address:{self.library_address}")

class Member:
    def __init__(self,member_id,member_name,member_contact):
        self.member_id = member_id
        self.member_name = member_name
        self.member_contact = member_contact
    def displayMemberDetails(self):
        print(f"Member ID:{self.member_id}\nMember Name:{self.member_name}\nMember Contact:{self.member_contact}")

class LibraryManagement(Library,Member):
    def __init__(self,library_name,library_address,member_id,member_name,member_contact):
        super().__init__(library_name,library_address)
        Member.__init__(self,member_id,member_name,member_contact)
    def displayLib(self):
        self.displayLibraryDetails()
        self.displayMemberDetails()

lm = LibraryManagement("Greenbelt Library","305,Pine Street",4762,"Hema",9832671639)
lm.displayLib()

#2.
class Restaurant:
    def __init__(self,restaurant_name,dish_name,price):
        self.restaurant_name = restaurant_name
        self.dish_name = dish_name
        self.price = price
    def displayRestaurantInfo(self):
        print(f"Restaurant Name:{self.restaurant_name}\nDish Name:{self.dish_name}\nPrice:{self.price}")

class Delivery:
    def __init__(self,rider_id,rider_name,rider_contact):
        self.rider_id = rider_id
        self.rider_name = rider_name
        self.rider_contact = rider_contact
    def displayDeliveryInfo(self):
        print(f"Rider Id:{self.rider_id}\nRider Name:{self.rider_name}\nRider Contact:{self.rider_contact}")

class Order(Restaurant,Delivery):
    def __init__(self,restaurant_name,dish_name,price,rider_id,rider_name,rider_contact):
        super().__init__(restaurant_name,dish_name,price)
        Delivery.__init__(self,rider_id,rider_name,rider_contact)
    def displayRes(self):
        self.displayRestaurantInfo()
        self.displayDeliveryInfo()

o = Order("The Food Corner","Chicken Noodles",200,"s323f6","Aadhvik",9416572618)
o.displayRes()
