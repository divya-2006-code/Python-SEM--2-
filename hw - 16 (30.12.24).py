#1.
class countCharacters:
    def __init__(self,string):
        alphabets=0
        numbers=0
        special_characters=0
        for char in string:
            if char.isalpha():
                alphabets+=1
            elif char.isdigit():
                numbers+=1
            elif not char.isalnum():
                special_characters+=1

        print(f"Alphabetic Characters count:{alphabets}")
        print(f"Numeric Characters count:{numbers}")
        print(f"Special Characters count:{special_characters}")

string=input("Enter the String:")
c=countCharacters(string)

#2.
class Stringvalidation:
    def __init__(self,s):
        self.s=s
        alphabets=0
        special_characters=0
        for char in self.s:
            if char.isalpha():
                alphabets+=1
            elif not char.isalnum():
                special_characters+=1
        if alphabets > 0 and special_characters > 0:
            print("The string contains both alphabets and special characters.")
        else:
            print("The string does not contain both alphabets and special characters.")

s = input("Enter the String: ")
v = Stringvalidation(s)

                

