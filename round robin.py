import random

print("Welcome to my round robin app")

teams=int(input("How many teams are there?: "))
team_list=[]
team_count=0
games=[]

def pick_teams(team_list):
    if teams % 2 == 0:
        even(team_list)
    else:
        odd(team_list)
        
def even(team_list):
    games = []
    half_list = int(len(team_list)/2)
    team1 = [i+1 for i in range(half_list)]
    team2 = [i+1 for i in range(half_list, len(team_list))][::-1]
    for i in range(len(team_list)-1):
        team1.insert(1, team2.pop(0))
        team2.append(team1.pop())
        for t in zip(team1, team2):
            games.append((team_list[t[0]-1], team_list[t[1]-1]))
    for x in games:
      print (*x, sep=" - ")
   
def odd(team_list):
    global matchcount
    games = []
    half_list = int((len(team_list)+1)/2)
    team1 = [i+1 for i in range(half_list)]
    team2 = [i+1 for i in range(half_list, len(team_list)+1)][::-1]
    for i in range(len(team_list)):
        team1.insert(1, team2.pop(0))
        team2.append(team1.pop())
        for t in zip(team1, team2):
            if len(team_list)+1 not in t:
                games.append((team_list[t[0]-1], team_list[t[1]-1]))
    for x in games:
      print (*x, sep=" - ")


for i in range (teams):
    team_count+=1
    entry=input("Type in name of team {}: ".format(i+1))
    team_list.append(entry)
    

print ("\nTeams you are willing to match: ", ", ".join(team_list),end=".\n")
random.shuffle(team_list)
print (len(team_list), "teams in total.")
if teams%2==0:
  global matches
  matches=(len(team_list)//2)*((len(team_list))-1)
else: 
  matches=((len(team_list)-1)*(len(team_list))//2)


if matches==1:
    print ("It will be one match only.")
else: 
    print ("It will be",matches,"matches in total.")
print("\n----------")
print("Fixtures are: \n")
    
pick_teams(team_list)

