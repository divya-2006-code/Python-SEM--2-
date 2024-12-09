#1.
class Camera:
    def __init__(self,resolution):
        self.resolution = resolution
    def Take_photo(self):
        print("Taking a photo with resolution:",self.resolution)

class Phone:
    def __init__(self,phone_number):
        self.phone_number = phone_number
    def make_call(self,number):
        print(f"A call to {number}")
    def send_message(self,number,message):
        print(f"Sending message:{message}to{number}")

class Smartphone(Camera,Phone):
    def __init__(self,resolution,phone_number,brand,model):
        Camera.__init__(self,resolution)
        Phone.__init__(self,phone_number)
        self.brand = brand
        self.model = model
    def display(self):
        print(f"Brand:{self.brand}")
        print(f"Model:{self.model}")
        print(f"Phone Number:{self.phone_number}")
        print(f"Camera Resolution:{self.resolution}")

p = Smartphone("Samsung","Galaxy S23","108MP",9765283524)
p.display()

#2.
class Student:
    def __init__(self,name,course):
        self.name = name
        self.course = course
    def Student_Info(self):
        print(f"Student Name:{self.name}\ncourse:{self.course}")

class StudentAthlete(Student):
    def __init__(self,name,course,sport):
        super().__init__(name,course)
        self.sport = sport
    def display_Athlete_Info(self):
        self.Student_Info()
        print(f"Sports Name:{self.sport}")

stu = StudentAthlete("Hema","Computer Science","Basketball")
stu.display_Athlete_Info()



