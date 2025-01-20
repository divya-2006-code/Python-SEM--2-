#1.
def reverse_string(s):
    return s[::-1]

print(reverse_string(input("Enter the string:")))

#2.

def  is_palindrome(s):
    s=s.lower()
    if len(s)<=1:
        return True
    elif s[0]!=s[-1]:
        return False
    else:
        return is_palindrome(s[1:-1])

s=input("Enter the string:")
print(is_palindrome(s))


#3.
def power(x,n):
    result=1
    for i in range(n):
        result*=x
    return result
print(power(5,3))

#4.
def sum_of_digits(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total
print(sum_of_digits(2023))

#5.
def sum_array(arr):
    total=0
    for row in arr:
        for num in row:
            total+=num
    return total

array=[[1,2,3],[4,5,6],[7,8,9]]
print(sum_array(array))

#6.
def transpose_matrix(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(transpose_matrix(matrix))




