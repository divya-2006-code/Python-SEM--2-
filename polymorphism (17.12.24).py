class Library:
    def issue_book(self,book_name,user):
        return f"Book issued:{book_name} to {user}"
    def returned_book(self,book_name,user):
        return f"Book returned is:{book_name} by {user}"

class DigitalLibrary(Library):
        def issue_book(self,book_name,user):
            return f"Book issued:{book_name} to {user}"
        def returned_book(self,book_name,user):
            return f"Book returned is:{book_name} by {user}"

lib = Library()
dig = DigitalLibrary()

book = input()
username = input()

print(lib.issue_book(book,username))
print(lib.returned_book(book,username))

print(dig.issue_book(book,username))
print(dig.returned_book(book,username))
