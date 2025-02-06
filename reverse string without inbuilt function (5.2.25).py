#reverse a string without using built-in function
"""m=input("enter a string:").strip() #divya
length=0
reverse=""
for i in m:
    length+=1 #5
for i in range(length-1,-1,-1):#(5-1,-1,-1)--->4,3,2,1,0 -->after it comes to 0 it stop the loop
    reverse+=m[i] # a| ay| ayv| ayvi| ayvid|
print("The reversed string is:",reverse)

#using function
def reverse_string(r):
    reverse=""
    length=0
    for i in n:
        length+=1
    for i in range(length-1,-1,-1):
        reverse+=n[i]
    return reverse
n=input("Enter a string:").strip()
rev=reverse_string(n)
print("The reverse string is :",rev)"""

#replace the letter in a given string
input_string=input("Enter a string:").strip()
to_replace=input("Enter a character to replace:")
replace_with=input("Enter a character to replace with:")

replaced_string=""
for c in input_string:
    if c==to_replace:
        replaced_string+=replace_with
    else:
        replaced_string+=c
print("Replaced string is:",replaced_string)
    
