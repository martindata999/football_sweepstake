import random

participants = [] 

football_teams = []

def assign_teams(list1, list2):
    random.shuffle(list2)
    pairs = {}
    for i, item in enumerate(list1):
        pairs[item] = list2[i]
    return pairs

assigned_teams = assign_teams(participants, football_teams)

print("Assigned Teams:")
for participant, team in assigned_teams.items():
    print(f"{participant}: {team}")