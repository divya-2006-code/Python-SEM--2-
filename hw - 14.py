class Ecommerce:
    def __init__(self,base_price,discount=0,tax=0):
        self.base_price=base_price
        self.discount=discount
        self.tax=tax
    def calculate_final_price(self):
        if self.base_price<0:
            raise ValueError("Base price cannot be negative")
        if self.discount<0:
            raise ValueError("Discount percentage cannot be negative")
        if self.tax<0:
            raise ValueError("Tax percentage cannot be negative")
        else:
            discount_amount=(self.discount/100)*self.base_price
            tax_amount=(self.tax/100)*self.base_price
            final_amount=self.base_price+tax_amount-discount_amount
            return final_amount

try:
    base_price=float(input("Enter the Original price of the product:"))
    discount=float(input("Enter the discount percentage:"))
    tax=float(input("Enter the tax percentage:"))
    product=Ecommerce(base_price,discount,tax)
    price=product.calculate_final_price()
    print(f"Total price:{price:.2f}")
except ValueError as e:
    print(e)

    
        
