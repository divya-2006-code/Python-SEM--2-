class Calculator:
    def calculate(self,a=None,b=None,c=None ):
        if c is not None:
            return a*b*c
        elif b is not None:
            return a+b
        elif a is not None:
            return a**2
        else:
            raise ValueError("Invalid number of arguments")
        
calc = Calculator()
print(calc.calculate(4))  # a = 4**2:16
print(calc.calculate(2, 3))  # a+b = 2+3: 5
print(calc.calculate(2, 5, 4))# a*b*c = 2*5*4: 40

