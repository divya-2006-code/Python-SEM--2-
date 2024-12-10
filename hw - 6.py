#1.

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def displayVehicleInfo(self):
        print(f"Make:{self.make}\nModel:{self.model}\nYear:{self.year}")

class Car(Vehicle):
    def __init__(self,make,model,year,doors,capacity):
        super().__init__(make,model,year)
        self.doors = doors
        self.capacity = capacity
    def displayCarInfo(self):
        self.displayVehicleInfo()
        print(f"Number of Doors:{self.doors}\nTrunk Capacity:{self.capacity}")

class Truck(Vehicle):
    def __init__(self,make,model,year,cargo_capacity,axles):
        super().__init__(make,model,year)
        self.cargo_capacity = cargo_capacity
        self.axles = axles
    def displayTruckInfo(self):
        print(f"Cargo Capacity:{self.cargo_capacity}\nNumber of Axles:{self.axles}")
        
class PickupTruck(Car,Truck):
    def __init__(self,make,model,year,doors,capacity,cargo_capacity,axles):
        Vehicle.__init__(self,make,model,year)
        self.doors = doors
        self.capacity = capacity 
        self.cargo_capacity = cargo_capacity
        self.axles = axles
    def displayPickupTruck(self):
        self.displayCarInfo()
        self.displayTruckInfo()

v = PickupTruck("Nissan","Navara",2022,4,400,1.8,2)
v.displayPickupTruck()


#2.

class Product:
    def __init__(self,product_Id,name,price):
        self.product_Id = product_Id
        self.name = name
        self.price = price
    def displayProductInfo(self):
        print(f"Product ID:{self.product_Id}\nName:{self.name}\nPrice: Rs.{self.price}")

class Electronics(Product):
    def __init__(self,product_Id,name,price,warranty,brand):
        super().__init__(product_Id,name,price)
        self.warranty = warranty
        self.brand = brand
    def displayElectronicsInfo(self):
        self.displayProductInfo()
        print(f"Warranty Period:{self.warranty}\nBrand:{self.brand}")

class Clothing(Product):
    def __init__(self,product_Id,name,price,size,material):
        super().__init__(product_Id, name, price)
        self.size = size
        self.material = material
    def displayClothingInfo(self):
        self.displayProductInfo()
        print(f"Size:{self.size}\nMaterial:{self.material}")

e = Electronics(101,"Laptop",55000,1,"Lenovo")
e.displayElectronicsInfo()
c = Clothing(201,"T-shirt",250,34,"cotton")
c.displayClothingInfo()


