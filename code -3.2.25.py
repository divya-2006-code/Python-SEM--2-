mul=lambda a,b,c:a*b*c
print(mul(2,3,4))

c=list(map(int,input().split()))
cube=map(lambda x:x**3,c)
print(list(cube))

l=list(map(int,input().split()))
odd=filter(lambda x:x%2!=0,l)
print(list(odd))

l=[(1,2),(4,5),(7,8)]
l1=sorted(l,key=lambda x:x[0])
print(l1)
