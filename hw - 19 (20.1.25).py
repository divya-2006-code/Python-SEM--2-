class BankAccount:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"Deposited ${amount}.New balance is $ {self.__balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self,amount):
        if amount>0 and amount<=self.__balance:
            self.__balance-=amount
            print(f"Withdrew $ {amount}.New balance is $ {self.__balance}")
        else:
            print("Invalid Withdrawal amount!")

    def add_interest(self,rate):
        interest=self.__balance*(rate/100)
        self.__balance+=interest
        print(f"Added $ {interest} interest.Current  balance is $ {self.__balance}")

    def get_account_number(self):
        return self.__account_number

    def get_balance(self):
        return self.__balance


account=BankAccount("123456789",1000)
print(f"Account Number:{account.get_account_number()}")
print(f"Balance: $ {account.get_balance()}")

account.deposit(500)
account.withdraw(200)
account.add_interest(5)
