arr=list(map(int,input("Enter the elements of the array separated by space:").split()))
print("The original array is :",arr)

print("\nElements at odd position:")
for i in range(len(arr)):
    if i%2!=0:
        print(f"Index:{i}, Value:{arr[i]}")

print("\nElements at even position:")
for i in range(len(arr)):
         if i%2==0:
             print(f"Index:{i}, Value:{arr[i]}")
         
