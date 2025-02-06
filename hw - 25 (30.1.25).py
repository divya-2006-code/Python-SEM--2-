#1.
import re

class User:
    def __init__(self):
        self.name=" "
        self.email=" "
        self.password=" "
        self.count=" "
    def validate_name(self,name):
        if re.match(r"^(?=.*[0-9])(?=.*[!@#$%^&*()_+])[A-Za-z0-9!@#$%^&*()_+]+$",name):
            return True
        return False

    def validate_password(self,password):
        if len(password)<=8 and re.match(r"^[A-Za-z#_@]+$",password):
            return True
        return False

    def validate_email(self,email):
        if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$",email):
            return True
        return False

    def get_user_input(self):
        while True:
            self.name=input("Enter your Name:")
            if self.validate_name(self.name):
                break
            print("Invalid Name! Must contain atleast one number and one special_character.")

        while True:
            self.password=input("Enter your Password:")
            if self.validate_password(self.password):
                break
            print("Invalid password! Must contain only letters and #,_,@,and be atmost 8 characters long.")

        while True:
            self.email=input("Enter your Email address:")
            if self.validate_email(self.email):
                break
            print("Invalid Email Format! Please enter a valid email.")

        while True:
            try:
                self.count=int(input("How many times do you want to print?"))
                if self.count>0:
                    break
                print("Enter a positive integer.")
            except ValueError:
                print("Invalid input! Enter a valid number.")

    def display_info(self):
        print(f"{self.name} wants to print {self.count} times and send mail to {self.email}")
        print(f"Your password {self.password} will be encrypted and stored.")

user=User()
user.get_user_input()
user.display_info()

#2.
class User:
    def __init__(self, name, department):
        self.name = name
        self.department = department
        self.password = None
        self.security_questions = {}

    def encode_name(self):
        return "X" * len(self.name) + " – Fresher"

    def is_valid_password(self, password):
        
        has_digit = any(char.isdigit() for char in password)
        has_special = any(not char.isalnum() for char in password)
        length = len(password) <= 8
        return has_digit and has_special and length

    def set_password(self):
        while True:
            password = input("Enter your Password: ")
            re_password = input("Re-Type your Password: ")

            if not self.is_valid_password(password):
                print("Password must contain at least one number, one special character, and be at most 8 characters long.")
                continue

            if password != re_password:
                print("Passwords do not match. Try again.")
                continue

            self.password = password
            print("Password successfully set.")
            break

    def set_security_questions(self):
        print("\nSet Security Questions:")
        self.security_questions["Q1"] = input("What is your favorite color? ")
        self.security_questions["Q2"] = input("What is your birth month? ")

    def forgot_password(self):
        print("\nAnswer security questions to retrieve your password.")
        for _ in range(3):  # Allow up to 3 attempts
            ans1 = input("What is your favorite color? ")
            ans2 = input("What is your birth month? ")

            if ans1 == self.security_questions["Q1"] and ans2 == self.security_questions["Q2"]:
                print(f"Your password is: {self.password}")
                return
            else:
                print("Incorrect answers. Try again.")

        print("Security verification failed. Please contact support.")

    def password_re_entry(self):
        attempts = 3
        while attempts > 0:
            entered_password = input("Re-enter your Password: ")
            if entered_password == self.password:
                print("Password accepted. Login successful.")
                return True
            else:
                print(f"Incorrect password. Attempts left: {attempts - 1}")
                attempts -= 1

        
        choice = input("\n1. Forgot Password\n2. Know Password\nEnter choice: ")
        if choice == "1" or choice == "2":
            self.forgot_password()
        else:
            print("Invalid choice. Exiting.")
 
name = input("Enter your Name: ")
department = input("Enter your Department: ")
 
user = User(name, department)    
print("\nYour Encoded Name is:", user.encode_name())
print("Your Department is:", user.department)

user.set_password()
user.set_security_questions()
user.password_re_entry()


            
