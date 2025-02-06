 #1.
f_name=input("Enter the first name:")
l_name=input("Enter the last name:")
clg_name=input("Enter the college name:")
department=input("Enter  the department:")
mobile_num=input("Enter the mobile number:")

full_name=f_name+" "+l_name
print(f"Your name is:{full_name}")

clg_details=clg_name+" "+department
print(f"Your College name:{clg_name} Department of {department}")

print("ASCII value name is:", end=" ")
for char in full_name:
    print(f"{char}-{ord(char)}", end=",")
print()

print("ASCII value for mobile number:", end=" ")
for char in mobile_num:
    print(f"{char}-{ord(char)}", end=",")
print()

print("Result of Addition:", end=" ")
for i in range(min(len(full_name),len(mobile_num))):
    addition=ord(full_name[i])+int(mobile_num[i])
    print(f"{full_name[i]}+{mobile_num[i]}= {addition}", end=", ")



#2.
num1=int(input("Enter the first value:"))
num2=int(input("Enter the second value:"))
num3=int(input("Enter the third value:"))
add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2
mod=num1%num2
print("\nArithmetic Operations:")
print("Addition:",add)
print("Subtraction:",sub)
print("Multiplication:",mul)
print("Division:",div)
print("Modulus:",mod)

print("\nBefore swapping:")
print(f"First value - {num1}")
print(f"Second value - {num2}")
print(f"Third value - {num3}")

num1,num2,num3=num2,num3,num1

print("\nAfter swapping:")
print(f"First value - {num1}")
print(f"Second value - {num2}")
print(f"Third value - {num3}")


#3.
#a. Remove numbers from username
first_name=input("Enter first name:")
filtered_name=''.join([char for char in first_name if not char.isdigit()])
print("Hi!Your Entered Input is ",filtered_name)

#b.
name=input("Enter Name:")
chars=''.join(char for char in name if char.isalpha())
special_chars=''.join(char  for char in name if not  char.isalnum())
print(f"Your entered characters are - {chars}")
print(f"Your entered special characters are - {special_chars}")


