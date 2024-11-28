#1.
class person: #parent class
    def __init__(self,name):
        self.name = name
    def show_name(self):
        print("Name =",self.name)

class student(person): #child class
    def __init__(self,name,student_id):
        super(). __init__(name)# initialize the attribute from parent class
        self.student_id = student_id
    def show_studentId(self):
        print("Student_Id =",self.student_id)

stu = student("Hema",235797)
stu.show_name()
stu.show_studentId()


#2.
class Employee: #parent class
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display_details(self):
        print("Name =",self.name,"\nSalary =",self.salary)

class Manager(Employee): #child class
    def __init__(self,name,salary,department):
        super(). __init__(name,salary) #initialize the attribute from parent class
        self.department = department

    def display_department(self):
        print("Department =",self.department)

m = Manager("Lavanya",80000,"IT") #object for child class
#show all details
m.display_details()
m.display_department()
        
