#1.
class Customer:
    def __init__(self,name,phone_no):
        self.name=name
        self.phone_no=phone_no
    def display_customer_details(self):
        print(f"Customer Name: {self.name}")
        print(f"Customer Phone Number: {self.phone_no}")
        print("--------------------------------------------------------------------------")

class Depositor(Customer):
    def __init__(self,name,phone_no,acc_no,balance):
        super().__init__(name,phone_no)
        self.acc_no=acc_no
        self.balance=balance
    def display_depositor_details(self):
        self.display_customer_details()
        print(f"Customer A/C No: {self.acc_no}")
        print(f"Balance: {self.balance}")
        print("----------------------------------------------------------------------------------")

class Borrower(Depositor):
    def __init__(self,name,phone_no,acc_no,balance,loan_no,loan_amount):
        super().__init__(name,phone_no,acc_no,balance)
        self.loan_no=loan_no
        self.loan_amount=loan_amount
    def display_borrower_details(self):
        self.display_depositor_details()
        print(f"Loan Number: {self.loan_no}")
        print(f"Loan Amount: {self.loan_amount}")
        print("--------------------------------------------------------------------------------")


customers=[]
n=int(input("\nEnter the number of customers:"))
for i in range(n):
    name=input("Enter name:")
    phone_no=input("Enter phone number:")
    acc_no=input("Enter account number:")
    balance=float(input("Enter balance:"))
    loan_no=input("Enter loan number:")
    loan_amount=float(input("Enter loan amount:"))
    customers.append(Borrower(name,phone_no,acc_no,balance,loan_no,loan_amount))
    print("*"*50)

print("\nDetails of customer:\n")
for customer in customers:
    customer.display_borrower_details()

#2.
num=list(map(int,input("Enter the array elements (0s and 1s) separated by space: ").split()))
max_len=0
n=len(num)

for i in range(n):
    count_0=0
    count_1=0
    for j in range(i,n):
        if num[j]==0:
            count_0 += 1
        else:
            count_1 += 1
    if count_0==count_1:
        max_len=max(max_len,j-i+1)
print(max_len)
