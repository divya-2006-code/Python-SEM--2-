"""#1.
n=int(input())
for i in range(1,n+1):
    num=i
    for j in range(i):
        print(num,end=" ")
        num+=(n-j-1)
    print()

#2.
arr=list(map(int,input().split()))
for i in arr:
    if arr.count(i)>len(arr)//2:
        print(i)
        break"""

#3.
class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks

    def average_marks(self):
        total_mark=sum(self.marks.values())
        num_sub=len(self.marks)
        return total_mark/num_sub

    def find_topper(self):
        topper=students[0]
        for student in students[1:]:
            if student.average_marks()>topper.average_marks():
                topper=student
        return topper

s1=Student("Anu",104,{"Math":70,"Tamil":60,"English":80})
s2=Student("Keerthi",104,{"Math":98,"Tamil":72,"English":85})
s3=Student("Moni",104,{"Math":75,"Tamil":63,"English":90})
students=[s1,s2,s3]

topper=Student.find_topper(students)

print(f"Topper: {topper.name} , Roll no: {topper.roll_no}, Average marks: {topper.average_marks():.2f}")

#4.
def product_info(name,brand,price,discount=None):
    print(f"Name: {name}")
    print(f"Brand: {brand}")
    print(f"Price: {price}")

    if discount is not None:
        final_price=price - (price*discount/100)
        print(f"Discount:{discount}%")
        print(f"Final price after discount:{final_price}")
    else:
        print("Discount not available")

product_info(name="Laptop", brand="Dell",price=80000,discount=10)

















































