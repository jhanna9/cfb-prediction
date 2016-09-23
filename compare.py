from links import build_dict
from schedule_spread import schedule
from sos_2016 import sos
from team_stat import team_stats

def match_team():
    '''

    '''
    # builds team schedule from covers
    teams = schedule()

    # builds dictionary of variation on team names
    team_var = build_dict('team_variation.txt')
    
    # list to return and list to place hold teams not in team_var
    teams_new = []
    no_list = []
    
    # iterates through teams and team_var
    x = 0
    for t in teams:
        ind = teams.index(t)
        x = 0
        '''if team from teams is appened to no_list, 
           following team is not added to team_var
        '''
        if teams[ind - 1] in no_list:
            continue
        for k, v in team_var.items():     
            if t in v:
                teams_new.append(k) # adds correct variation of team name to list
                x = 0
                break
            elif x == len(team_var) - 1:
                no_list.append(t)          
            else:
                x += 1
            
    return teams_new
