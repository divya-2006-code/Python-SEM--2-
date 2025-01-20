from abc import ABC,abstractmethod

#Abstract class

class Employee(ABC):
    def __init__(self,name):
        self.name=name
    @abstractmethod
    def calculate_pay(self): 
        pass


#Concrete class for salaried employees:

class SalariedEmployee(Employee):
    def __init__(self,name,annual_salary):
        super().__init__(name)
        self.annual_salary=annual_salary

    def calculate_pay(self):
        return self.annual_salary/12

#concrete class for hourly employees

class HourlyEmployee(Employee):
    def __init__(self,name,hours_worked,hourly_rate):
        super().__init__(name)
        self.hours_worked=hours_worked
        self.hourly_rate=hourly_rate

    def calculate_pay(self):
        return self.hours_worked*self.hourly_rate

n=input("Enter your Name:")
ann_sal=float(input("Enter annual amount:"))
s=SalariedEmployee(n,ann_sal)
print(f"Salalried employee ({n}) Pay:${ann_sal:.2f}")


n=input("Enter your name:")
hour_work=float(input("Enter working hours:"))
hour_rate=float(input("Enter hour rate:"))
h=HourlyEmployee(n,hour_work,hour_rate)
print("Hour Employee:",n)
print("Pay:",s.calculate_pay())
print("Pay:",h.calculate_pay())

 
