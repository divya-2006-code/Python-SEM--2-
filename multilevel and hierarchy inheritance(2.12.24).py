#1.Multilevel Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id = Id
    def displayEmployee(self):
        self.displayPerson()
        print("Id:",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age,Id)
        self.salary = salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary:",self.salary)

per = Manager("Hema",30,465,50000)
per.displayManager()

#Hierarchy Inheritance
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def displayPerson(self):
        print(f"Name:{self.name}\nAge:{self.age}")

class Employee(Person):
    def __init__(self,name,age,Id):
        super().__init__(name,age)
        self.Id = Id
    def displayEmployee(self):
        self.displayPerson()
        print("ID:",self.Id)

class Manager(Employee):
    def __init__(self,name,age,Id,salary):
        super().__init__(name,age,Id)
        self.salary = salary
    def displayManager(self):
        self.displayEmployee()
        print("Salary:",self.salary)

per = Manager("Lavanya",30,245,40000)
per.displayManager()


    
