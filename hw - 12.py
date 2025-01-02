"""def int_to_roman(num):
    roman_numerals=[("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]
    roman_result=''

    for symbol,value in roman_numerals:
        while num>=value:
            roman_result+=symbol
            num-=value
    return roman_result
print(int_to_roman(9))
print(int_to_roman(100))
print(int_to_roman(22))"""


roman_symbols=[("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]
symbol=input("Enter the symbol: ")
result=0
for v,s in roman_symbols:
    for n in symbol:
        if n==v:
            result+=s
print(result)






















"""num=int(input("Enter the number:"))
roman_value=[("M",1000),("CM",900),("D",500),("CD",400),("C",100),("XC",90),("L",50),("XL",40),("X",10),("IX",9),("V",5),("IV",4),("I",1)]
result=''

for symbol,value in roman_value:
    while num>=value:
            result+=symbol
            num-=value

print(result)"""




        
