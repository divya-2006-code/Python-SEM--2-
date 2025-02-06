#1.
def validate_username():
    while True:
        name = input("Enter your Name: ")
        if name.isalpha():
            return name
        else:
            print("Invalid name. Please enter only letters and spaces.")

def validate_department():
    while True:
        department = input("Enter your Department: ")
        if department.strip():  # Ensures department is not empty
            return department
        

def validate_password():
    while True:
        password = input("Enter your password: ")
        if len(password) <= 8 and any(char.isdigit() for char in password):
            return password
        else:
            print("Invalid password. Please enter a password with at least one number and not more than 8 characters.")

def validate_re_password(password):
    while True:
        re_password = input("Re-enter your password: ")
        if re_password == password:
            return re_password
        else:
            print("Passwords do not match. Please try again.")

def display_details():
    name = validate_username()
    department = validate_department()
    password = validate_password()
    re_password = validate_re_password(password)

    encoded_name = "X" * len(name)
    encoded_department = "X" * len(department)
    encoded_password = "X" * len(password)
    encoded_re_password = "X" * len(re_password)

    print(f"Your Encoded Name is: {encoded_name} - Fresher")
    print(f"Your Department is: {encoded_department}")
    print(f"Your Password is: {encoded_password}")
    print(f"Re-Type your Password: {encoded_re_password}")

display_details()






#2.

a=[1,3,5,3,7,1,9,3]
print("Original array :",a)
a.remove(3)
print("New array:",a)

#3.
arr=["Face","Prep","Campus","Tech","Solutions"]
print("Your Non-Inverse order array is - ",arr)
inverse_arr=arr[::-1]
print("Your Inverse Order array is - ",inverse_arr)
