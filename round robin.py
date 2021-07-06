import random

print("Welcome to my round robin app")

teams=int(input("How many teams are there?: "))
team_list=[]
team_count=0
round=0

def pick_teams(teams):
    if len(teams) % 2 == 0:
        pick_even(team_list)
    else:
        pick_odd(team_list)



for i in range (teams):
    team_count+=1
    entry=input("Type in name of team {}: ".format(i+1))
    team_list.append(entry)
    

print ("\nTeams you are willing to match: ",*team_list, sep = ", ")
random.shuffle(team_list)
print (len(team_list), "teams in total")
matches=(len(team_list)//2)*((len(team_list))-1)
if matches==1:
    print ("It will be",matches,"match only")
else: 
    print ("It will be",matches,"matches in total")
print("\n----------")
    


