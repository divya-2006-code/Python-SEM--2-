import re
def verify_password(password):
    ex=r'^(?=.+[a-z A-Z]*\d*[asd])(?!.[(!@#$%^&*()_-+=)]).{8,}$'

    if re.match(ex,password):
        print("Password is strong")
    else:
        print("Password is not strong")


password=input("Enter the Password:")
verify_password(password)
