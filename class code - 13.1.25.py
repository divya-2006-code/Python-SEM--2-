#1.
n=int(input("Enter the number of elements :"))
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
non_zero_index=0
for i in range(len(l)):
    if l[i]!=0:
        l[non_zero_index],l[i]=l[i],l[non_zero_index]
        non_zero_index+=1

print("Updated array:",l)


#2.
n = int(input("Enter the number of elements: "))
l = []
for i in range(n):
    a = int(input())
    l.append(a)

zero_index = 0

for i in range(len(l)):
    if l[i] == 0:
        l[zero_index], l[i] = l[i], l[zero_index]
        zero_index += 1

print("Updated array:", l)

#3.
def maxProfit(prices):
   max_profit = 0
   for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1] #Compare prices[1] (1) with prices[0] (7): No profit, skip.
                                                                                  #Compare prices[2] (5) with prices[1] (1): Profit = 5-1=4,add to max_profit.
   return max_profit                                             #Compare prices[3] (3) with prices[2] (5): No profit, skip.
                                                                                 #Compare prices[4] (6) with prices[3] (3): Profit=6-3=3,add to max_profit.
                                                                                #Compare prices[5] (4) with prices[4] (6): No profit, skip.
prices =[7, 1, 5, 3, 6, 4]                                  #total =4+3=7
result = maxProfit(prices)
print(result) #7
