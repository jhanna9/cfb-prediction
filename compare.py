from links import build_dict
from schedule_spread import schedule
from sos_2016 import sos
from team_stat import team_stats

def match_team():
    '''

    '''
    teams = schedule()
    print(teams)
    print(len(teams))
    team_var = build_dict('team_variation.txt')
    teams_new = []
    no_list = []
    
    x = 0

    for t in teams:
        ind = teams.index(t)
        x = 0
        if teams[ind - 1] in no_list:
            continue
        for k, v in team_var.items():     
            if t in v:
                teams_new.append(k)
                x = 0
                break
            elif x == len(team_var) - 1:
                no_list.append(t)          
            else:
                x += 1
    
    print(len(teams_new))
            
    return teams_new

print(match_team())
#match_team()
