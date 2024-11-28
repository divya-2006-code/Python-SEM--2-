class student:
    def __init__(self,name,roll_no,s1,s2,s3):
        self.name = name
        self.roll_no = roll_no
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
    def grade(self):
        self.percentage = ((self.s1+self.s2+self.s3)/3)*100
        if self.percentage >= 85:
           print("grade S")
        elif self.percentage >= 75:
           print("grade A")
        elif self.percentage >= 65:
           print("grade B")
        elif self.percentage >= 55:
           print("grade C")
        elif self.percentage >= 50:
           print("grade D")
        else:
           print("grade F")

s = student("Divya",37473,60,78,83)
s.grade()



class Student:
    def __init__(self,name,age,course,grade):
        self.name = name
        self.age = age
        self.course = course
        self.grade = grade
    def __del__(self):
        print("The object has been deleted")
    def show(self):
        print("Student Info")
        print(f"Name:{self.name}\nAge:{self.age}\nCourse:{self.course}\nGrade:{self.grade}")
stu = Student("Hema",18,"Computer Application","A")
stu.show()
del stu
