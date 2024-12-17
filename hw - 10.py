#1.

class Login_system:
    def __init__(self,username,password):
        self.__username = username
        self.__password = password
    def set_password(self):
        if len(self.__password)< 8:
            print("Password must be atleast 8 characters long")
            return False
        if not any(char.isdigit()for char in self.__password):
            print("Password must contain atleast one number")
            return False
        if not any(char in "!@#$%^&*()-_+=<>?/|\\{}[]:;\"\'" for char in self.__password):
            print("Password must contain atleast one special character")
            return False
        return True
    def check_password(self):
        if self.set_password() == True:
            print("Password is Valid")
        else:
            print("Password Invalid!....Try again later...")

username = input("Enter the Name:")
password = input("Enter the Password:")
s = Login_system(username,password)
s.check_password()

#2.
class Product:
    def __init__(self,name,price,stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    def set_price(self,price):
        if price>0:
            self.__price = price
        else:
            print("Price must be greater than 0")
    def set_stock(self,stock):
        if stock  == int(stock) and stock >= 0:
            self._stock = stock
        else:
            print("Stock must be non - negative integer")
    def get_stock(self):
        return self.__stock

name = input("Enter the Product Name:")
price = int(input("Enter the Product Price:"))
stock = int(input("Enter the Stock:"))
pro = Product(name,price,stock)
print(f"Stock:{pro.get_stock()}")

#3.
class Student:
    def __init__(self,name,age,marks):
        self.__name = name
        self.__age = age
        self.__marks = marks
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        if 5 <= age <= 100:
            self.__age = age
        else:
            raise ValueError("Age must be in 5 and 100")
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0 <= marks <= 100:
            self.__marks = marks
        else:
            raise ValueError("Marks must be between 0 and 100")

try:
    name = input("Enter the Name:")
    age = int(input("Enter the Age:"))
    marks = int(input("Enter the Marks:"))
    stu = Student(name,age,marks)
    stu.set_age(age)
    stu.set_marks(marks)
    print(f"Name:{stu.get_name()}\nAge:{stu.get_age()}\nMarks:{stu.get_marks()}")

except ValueError as e:
    print(e)
                
              
        
    
        
