import re
import random

class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def verify_email(self):
        ex = r'^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$'
        if re.match(ex, self.email):
            print("Valid email id format")
        else:
            print("Invalid email id format")

    def verify_number(self):
        Id = r'^LIB\d{4}$'
        if re.match(Id, self.member_id):
            print("Valid member id")
        else:
            self.generate_id()

    def generate_id(self):
        self.member_id = "LIB" + str(random.randint(1000, 9999))
        print("Generated new member id:", self.member_id)

class Library(Member):
    def __init__(self, member_id, name, email, book_id, title, author):
        super().__init__(member_id, name, email)
        self.book_id = book_id
        self.title = title
        self.author = author

    def display(self):
        print("\nLibrary Member Details:")
        print("Member Id:", self.member_id)
        print("Name:", self.name)
        print("Email:", self.email)
        print("Book Id:", self.book_id)
        print("Title:", self.title)
        print("Author:", self.author)

if __name__ == "__main__":
    # Input details
    member_id = input("Enter the member Id: ")
    name = input("Enter the Name: ")
    email = input("Enter the Email: ")
    book_id = input("Enter the Book Id: ")
    title = input("Enter the Title of the Book: ")
    author = input("Enter the Author of the Book: ")

    # Create Library object and perform actions
    lib = Library(member_id, name, email, book_id, title, author)
    lib.verify_email()
    lib.verify_number()
    lib.display()
