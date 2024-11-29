class Employee:
    def __init__(self,name,Id,position):
        self.name = name
        self.Id = Id
        self.postion = position
    def displayEmployeeInfo(self):
        print(f"Name:{self.name}\nId:{self.Id}\nPosition:{self.postion}")

class Address:
    def __init__(self,street,state,country):
        self.street = street
        self.state = state
        self.country = country
    def displayAddressInfo(self):
        print(f"Street Name:{self.street}\nState Name:{self.state}\nCountry Name:{self.country}")

class EmployeeDetails(Employee,Address):
    def __init__(self,name,Id,position,street,state,country):
        super().__init__(name,Id,position)# super allow to access the attributes from parent class
        Address.__init__(self,street,state,country)
    def displayEmp(self):
        self.displayEmployeeInfo()
        self.displayAddressInfo()

ed = EmployeeDetails("Hema",3456,"Manager","Shenoy Nagar","TamilNadu","India")
ed.displayEmp()
