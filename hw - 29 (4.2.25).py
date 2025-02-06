#1.
s=input("Enter a string:")
s=s.strip()
word=s.split()
last_word=word[-1]
length_word=len(last_word)
print("Last word count is:",length_word)

#2.
m=input("Enter a first binary string:")
n=input("Enter a second binary string:")
sum_binary=bin(int(m,2)+int(n,2))[2:]
print("Sum of binary string:",sum_binary)
