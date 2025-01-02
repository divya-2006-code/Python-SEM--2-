#
list1=[2,5,7,4,8,35,23]
list2=[8,9,1,7,6,35]
common=[]

for elements in list1:
    if elements in list2:
        common.append(elements)
print("Common Elements:",common)

#
text=input("Enter the String:")
words=text.split()
count=0
for i in words:
    count+=1
print(count)

#
n=int(input("Enter the number:"))
sum_digits=0
while n!=0:
    rem=n%10
    sum_digits+=rem
    n//=10
print(sum_digits)

#
numbers=[3,6,8,2,7,8,2,76,34,7]
unique_numbers=[]
for i in numbers:
    if i not in unique_numbers:
        unique_numbers.append(i)
unique_numbers.sort(reverse=True)
print(unique_numbers)
nums = [3, 1, 4, 1, 5, 9]
def custom_sort(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                return nums
print(custom_sort(nums))

#
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance
    def deposit(self, amount):self.balance += amount
    return f"Deposited: {amount}, Balance: {self.balance}"
    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        self.balance-= amount
        return f"Withdrawn: {amount}, Balance: {self.balance}"
    def check_balance(self):
        return f"Balance: {self.balance}"
account = BankAccount()
print(account.deposit(100))
print(account.withdraw(50))
print(account.check_balance())

#
import re
def is_valid_email(email):
    return bool(re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email))
print(is_valid_email("example@test.com"))

#
import re
def extract_phone_numbers(text):
    return re.findall(r'\b\d{10}\b', text)
print(extract_phone_numbers("Call me at 1234567890 or 9876543210."))

#
import re
def extract_hashtags(text):
    return re.findall(r'#\w+', text)
print(extract_hashtags("Loving the weather!sunnyday #happiness"))

#
login_attempts = {}
while True:
    username = input("Enter your username: ")
    success = input("Was the login successful? (yes/no): ").lower()
    if username not in login_attempts:
        login_attempts[username] = 0 # Initialize attempts for a new user
        if success == "no":
            login_attempts[username] += 1
            if login_attempts[username] >= 5:
                print(f"Account locked for {username} after 5 failed attempts.")
                break
            else:
                print(f"Failed attempts for {username}: {login_attempts[username]}")
        elif success == "yes":
            print(f"Login successful for {username}.")
            login_attempts[username] = 0 # Reset attempts on successful login
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    


    
