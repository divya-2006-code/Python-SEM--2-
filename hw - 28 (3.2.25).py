#Sorting a dictionary using lambda 
stu_marks={"Anu":88,"Hema":69,"Moni":80,"Nithya":77,"Lavanya":95}

#1.
asc=dict(sorted(stu_marks.items(),key=lambda x:x[1]))
print("Ascending order:",asc)

#2.
desc=dict(sorted(stu_marks.items(),key=lambda x:x[1], reverse=True))
print("\nDescending order:",desc)

#3.
top3_stu=dict(sorted(stu_marks.items(),key=lambda x:x[1], reverse=True)[:3])
print("\nTop 3 students:",top3_stu)

#4.
sort_name=dict(sorted(stu_marks.items(),key=lambda x:x[0]))
print("\nSort students by name:",sort_name)

#Sorting a List of tuples using lambda
players=[("Messi",30),("Ronaldo",28),("Neymar",25),("Mbappe",35),("Salah",22)]

#1.
asc=sorted(players,key=lambda x:x[1])
print("Score in ascending order:",asc)

#2.
desc=sorted(players,key=lambda x:x[1],reverse=True)
print("\nScore in descending order:",desc)

#3.
top3_players=sorted(players,key=lambda x:x[1],reverse=True)[:3]
print("\nTop 3 goal scores:",top3_players)

#4.
sort_name=sorted(players,key=lambda x:x[0])
print("\nSort players by name:",sort_name)

#Find employees earning more than $5000.

#5.
emp=[("Aishu",5000),("Charu",3000),("Ramya",4000),("Zara",6000),("Dhanya",5400)]
earning=list(filter(lambda x:x[1] > 5000, emp))
print("\nEmployees earning more than $5000:",earning)
