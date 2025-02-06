"""#convert the character into lower case
character=input()
if 'A'<=character<='Z':
    c=ord(character)+32 
    converted=chr(c)
print(converted)

#convert the character into upper case
character=input()
if 'a'<=character<='z':
    c=ord(character)-32
    converted=chr(c)
print(converted)

#convert a string in lowercase
string=input()#DiV
for i in string:
    if 'A'<=i<='Z':
        p=ord(i)
        q=chr(p+32)
        print(q,end="")
    else:
        print(i,end="")

#convert the upper into lower and lower into upper
def lowercase(character):
    p=ord(character)
    q=chr(p+32)
    print(q,end="")
def uppercase(char):
    a=ord(char)
    b=chr(a-32)
    print(b,end="")

string=input("Enter the string:")
for i in string:
    if 'A'<=i<='Z':
        lowercase(i)
    elif 'a'<=i<='z':
        uppercase(i)"""

#List of string -->convert to lowercase
list1=["MANGO","APPLE","PINE","STRAWBERRY"]
lower=[]
for string in list1:
    lower_string=""
    for char in string:
        if "A"<=char<="Z":
            lower_string+=chr(ord(char)+32)
        else:
            lower_string+=char
    lower.append(lower_string)
print(lower)

#List of string -->convert to uppercase
list1=["cherry","plum","fig","blueberry"]
upper=[]
for string in list1:
    upper_string=""
    for char in string:
        if "a"<=char<="z":
            upper_string+=chr(ord(char)-32)
        else:
            upper_string+=char
    upper.append(upper_string)
print(upper)

#List of string -->mixed of upper and lower case
list1=["ManGo","ApPle","PlUm","CherRy"]
upper_lower=[]
for string in list1:
    upper_lower_string=""
    for char in string:
        if "A"<=char<="Z":
            upper_lower_string+=chr(ord(char)+32)
        elif "a"<=char<="z":
            upper_lower_string+=chr(ord(char)-32)
    upper_lower.append(upper_lower_string)

print(upper_lower)
