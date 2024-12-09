class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def Person_Info(self):
        print(f"Name={self.name}\nAge={self.age}")

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id=Id
    def Employee_Info(self):
        self.Person_Info()
        print(f"Id={self.Id}")

class Manager(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def Manager_Info(self):
        self.Person_Info()
        print(f"Salary={self.salary}")
        

class HR(Employee):
    def __init__(self,name,age,Id):
        Employee.__init__(self,name,age,Id)
    def HR_Info(self):
        self.Employee_Info()
    

a=HR("Hema",30,232)
a.HR_Info()

