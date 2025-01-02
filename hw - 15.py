class simpleCalculator:
    def add(self,m,n):
        return m+n
    def subtract(self,m,n):
        return m-n
    def multiply(self,m,n):
        return m*n
    def divide(self,m,n):
        if n==0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return m/n

def main():
    calculator=simpleCalculator()
    while True:
        try:
            m=float(input("Enter the first number:"))
            n=float(input("Enter the second number:"))
            operation=input("Entet the operation(+,-,*,/):")

            if operation=='+':
                result=calculator.add(m,n)
            elif operation=='-':
                result=calculator.subtract(m,n)
            elif operation=='*':
                result=calculator.multiply(m,n)
            elif operation=='/':
                result=calculator.divide(m,n)
            else:
                print("Invalid operation.Try again.......")
                continue
            print(f"The result is :{result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError as ec:
            print(ec)

if  __name__=="__main__":
    main()
            
            
                                                           
                                                           
                                                           
                                                           
                                                                       
