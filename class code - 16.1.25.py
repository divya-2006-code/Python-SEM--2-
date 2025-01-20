#1.
arr=[1,2,4,5]
n=len(arr)+1 #n=(length(arr)+miss_num)=4+1=5
total=n*(n+1)//2 #t=5*(5+1)//2=5*(6)//2=5*3=15
s=sum(arr) #s=[1+2+4+5=12]
miss_num=total-s #15-12=3
print("missing number is",miss_num) #3

#2.
arr=[4,3,2,7,8,2,3]
count={}

for num in arr:#n=4 #3 #2 #7 #8 #2 #3
    if num in count:
        count[num]+=1#{2:2,3:2}
    else:
        count[num]=1 #{4:1,7:1,8:1}

for num in count:
    if count[num]==1:
        print("appear once",num)

#3.
arr=[1,2,3,4]

if arr==sorted(arr):
    print(True)
else:
    print(False)

#4.
arr=[3,4,3,2,3,4,4,3,4,2,4]
count={}

for  num in arr:
    if num in count:
        count[num]+=1
    else:
        count[num]=1

n=len(arr)
for num in count:
    if count[num]>n//2:
        print("majority element is ",num)
#5.
arr=[1,2,3,4,10,1,2,3]
for i in range(len(arr)):
    left_sum=sum(arr[:i])
    right_sum=sum(arr[i+1:])

    if left_sum==right_sum:
        print(True)
        break
    else:
        print(False)
        

#6.
arr=[2,4,3,5,7,8]
target=10
pairs=[]

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            pairs.append((arr[i],arr[j]))

print(pairs)
        
        
