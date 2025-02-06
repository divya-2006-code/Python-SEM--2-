#1.
def longest_common_prefix(string):
    if not string:
        return ""
    prefix=string[0]

    for strs in string[1:]:
        while not strs.startswith(prefix):
            prefix=prefix[:-1]
            if not prefix:
                return ""
    return prefix
s=input("Enter a string:").split()
res=longest_common_prefix(s)
print("The longest common prefix in the string is:",res)

#2.
def is_subsequence(m,n):
    a,b=0,0
    while a<len(m) and b<len(n):
        if m[a]==n[b]:
            a+=1
            b+=1
        else:
            b+=1
    return a==len(m)
m=input("Enter a string 1:")
n=input("Enter a string 2:")
result=is_subsequence(m,n)
print("The final result is:",result)
