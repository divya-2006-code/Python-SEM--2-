#1.
gas=list(map(int,input("Enter the gas values:").split())) # 2 3 4
cost=list(map(int,input("Enter the cost values:").split())) # 3 4 3

if len(gas)!=len(cost):
    print("gas and cost values must be same length!")
else:
    n=len(gas)
    total_gas=0
    total_cost=0
    current_tank=0
    starting_station=0

    for i in range(n): 
        total_gas+=gas[i] 

        total_cost+=cost[i] 

        current_tank+=gas[i]-cost[i] 

        if current_tank<0:
            starting_station=i+1
            current_tank=0

    if total_gas>=total_cost:
        print(starting_station)
    else:
        print(-1)

#2.

ratings=list(map(int,input("Enter the ratings:").split()))
n=len(ratings)
candies=[1]*n 

for i in range(1,n):
    if ratings[i]>ratings[i-1]:
        candies[i]=candies[i-1]+1

for i in range(n-2,-1,-1):
    if ratings[i]>ratings[i+1]:
        candies[i]=max(candies[i],candies[i+1]+1)

total_candies=sum(candies)

print(total_candies)

            
        


    
    
