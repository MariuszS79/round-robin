import random

print("Welcome to my round robin app")

teams=int(input("How many teams are there?: "))
team_list=[]
team_count=0

for i in range (teams):
    team_count+=1
    entry=input("Type in name of team {}: ".format(i+1))
    team_list.append(entry)
    

print("Teams you are willing to match: ",*team_list, sep = ", ")