"""class Student:
    id = 342 #this is public one(no underscore) & __342 --> this is private one(double underscore)it show error
    def __init__(self,name):
        self.__name = name
    def display(self):
        print("Name =",self.__name)

s = Student("Ria")
s.display()
print(s.id)


class Student:
    id = int(input())
    __age = int(input())
    def __init__(self,name):
        self.__name = name
    def display(self):
        print("Name:",self.__name)

s = Student("Hema")
s.display()
print(s.id)
print("Age:",s._Student__age)

class Employee:
    def __init__(self,name,salary):
        self.name = name #Public variable
        self.__salary = salary #Private variable

emp = Employee("Lisa",10000)
print("Name:",emp.name)
print("Salary:",emp._Employee__salary)"""#To access private variable using object followed by single underscore and class name with double underscore variable. 


class Employee:
    def __init__(self,name,age,eid,gender,salary):
        self.__name = name
        self.age = age
        self.eid = eid
        self.__gender = gender
        self.salary = salary
    def displayEmployeeInfo(self):
        print("Name:",self.__name)
        print("Age:",self.age)
        print("Employee Id:",self.eid)
        print("Gender:",self.__gender)
        print("Salary:",self.salary)



emp = Employee("Jenifer",25,978,"Female",30000)
emp.displayEmployeeInfo()

