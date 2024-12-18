class Book:
    def __init__(self,pages):
        self.pages = pages
    #Overloading +operator with magic method
    def __add__(self,other):
        return self.pages + other.pages
b1 = Book(500)
b2 = Book(500)

print("Total number of Pages:",b1+b2)


#
class Addition:
    def add(self,a,b,c = 0):
        result = 0
        result = a+b+c
        return result

ad = Addition()
ans = ad.add(2,3)
print(ans)
ans1 = ad.add(2,3,4)
print(ans1)
