from links import build_dict
from schedule_spread import schedule
from sos_2016 import sos
from team_stat import team_stats

def match_team():
    '''

    '''
    teams = schedule()
    #print(teams)
    #print(len(teams))
    team_var = build_dict('team_variation.txt')
    teams_new = []
    skip = False
    x = 0
    y = 0
    
    print(team_var)

    '''with open(file) as f:
        for line in f:
            (val1, val2, val3) = line.split(',')
            team_var.append((val1, val2, val3.strip()))
           
    for t in teams:
        if skip == True:
                skip = False
                continue
        elif t not in team_var:
                skip = True
                continue
        else:
             teams_new.append(teams.index(t) - 1)
    ''''    

    #print(len(teams_new))
            
    return team_var

#print(match_team('team_variation.txt'))
match_team()
