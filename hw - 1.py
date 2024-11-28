class BankAccount:
    def __init__(self,name,account_num,balance):
        self.name = name
        self.account_num = account_num
        self.balance = balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
    def withdraw(self,amount):
        if amount<self.balance:
            self.balance-=amount
        else:
            print(f"Withdrawal amount must be greater than 0")
    def check_balance(self):
        print(f"Current balance:{self.balance}")
        
A1 = BankAccount("Hema",35467892780,50000)
A1.deposit(5000)
A1.withdraw(15000)
A1.check_balance()










class Cosmetics:
    def __init__(self,name="Lipstick",brand="Maybelline",price=250,category="makeup"):
      self.name = name
      self.brand = brand
      self.price = price
      self.category = category
    def show(self):
        print(f"Name = {self.name}\nBrand = {self.brand}\nPrice = {self.price}\nCategory = {self.category}")
pro = Cosmetics("Eyeliner", "Lakme",200,"Makeup")
pro.show()
p = Cosmetics()
p.show()

    
        
