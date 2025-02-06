#1.
from abc import ABC, abstractmethod

class WTS(ABC):
    @abstractmethod
    def welcome(self):
        pass

    @abstractmethod
    def test_data(self,name):
        pass

    @abstractmethod
    def count_vowels(self,name):
        pass

    @abstractmethod
    def calculate_grade(self,name,mark1,mark2):
        pass

class Student(WTS):
    def welcome(self):
        print("Welcome to WTS! We wish you the best!!")

    def test_data(self,name):
        print(f"Welcome {name} ! Have a nice day !")

    def count_vowels(self,name):
        vowels="aeiouAEIOU"
        name=name.lower()
        vowel_count={v: name.count(v)  for v in vowels if v in name}
        total_vowels=sum(vowel_count.values())
        
        print(f"Count of Vowels are:{total_vowels}")
        for vowel,count in vowel_count.items():
            print(f"{vowel} : {count}")

    def calculate_grade(self,name,mark1,mark2):
        total_marks=mark1+mark2
        if total_marks > 95:
            grade = 'E'
        elif 80<= total_marks <=95:
            grade = 'A+'
        elif 75> total_marks >=60:
            grade = 'A'
        elif 60 > total_marks >=50:
            grade = 'B'
        else:
            grade = 'F'

        print(f"Total Marks for {name}: {total_marks}")
        print(f"Grade : {grade}")

if __name__=="__main__":
    stu = Student()
    stu.welcome()

    name=input("Please input a name:")
    stu.test_data(name)
    stu.count_vowels(name)

    mark1=int(input("Enter Mark1: "))
    mark2=int(input("Enter Mark2: "))
    stu.calculate_grade(name,mark1,mark2)

#2.
password=input("Enter your input:")
result=" "

for char in password:
    if char.isdigit():
        break
    result+=char

print("Your output will Break here - ",result)

password=input("Enter your input:")
result=" "

for char in password:
    if not char.isdigit():
        result+=char

print("Your output will continue here - ",result)
    
