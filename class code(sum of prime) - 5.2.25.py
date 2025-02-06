"""numbers=list(map(int,input("Enter a numbers by space separated:").split())) 
total=0

for n in numbers:
    if n<2:
        f=False
    else:
        f=True
        for i in range(2,n):
            if n%i==0:
                f=False
                break

        if f:
            total+=n
print("Sum of prime numbers is:",total)"""

#Using function to add the prime numbers only
def is_prime(p):
    if p<2:
        return False
    if p==2:
        return True
    for i in range(2,p):
        if p%i==0:
            return False
    return True

    
def sum_digits(s):
    total=0
    for  i in str(s):
        if is_prime(int(i)): #(--->means "True") is_prime--->function call
            total+=int(i)
    return total



n=int(input())
result=sum_digits(n)
print(result)



"""def sum_prime():
    total=0
    for n in numbers:
        if n<2:
            f=False
        else:
            f=True
            for i in range(2,n):
                if n%i==0:
                    f=False
                    break
            if f:
                total+=n
    print(total)

numbers=list(map(int,input("enter a numbers by space separated:").split()))
sum_prime()

def sum_prime(p):
    total=0
    for n in numbers:
        if n<2:
            f=False
        else:
            f=True
            for i in range(2,n):
                if n%i==0:
                    f=False
                    break
            if f:
                total+=n
    return total

numbers=list(map(int,input("enter a numbers by space separated:").split()))
s_p=sum_prime(numbers)
print("The sum of prime numbers :",s_p)"""
