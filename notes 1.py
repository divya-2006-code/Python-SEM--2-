"""class Book:
    def __init__(self):
        self.name="Animal Farm"
        self.author="George Orwell"
    def show(self):
        print(f'Name={self.name}\nAuthor={self.author}')
b=Book()
b.show()"""

class Book:
    def __init__(self,book_name,author_name):
        self.name=book_name
        self.author=author_name
    def show(self):
        print(f'Name={self.name}\nAuthor={self.author}')
b=Book("Animal Farm","George Orwell")
b.show()

class Student:
    def __init__(self,name,age=12,classroom=7):
        self.name=name
        self.age=age
        self.classroom=7
    def show(self):
        print(self.name,self.age,self.classroom)
stu1=Student("Hema",12,7)
stu1.show()
