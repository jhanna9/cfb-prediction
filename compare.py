from links import build_dict
from schedule_spread import schedule
from sos_2016 import sos
from team_stat import team_stats

def match_team(teams):
    '''

    '''
    # builds team schedule from covers
    #teams = schedule()

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

def compare_stats():
    '''

    '''
    teams = match_team(schedule())
    strength = match_team(sos())
    print(strength)
    x = 0
        
    # use this loop for comparison
    for ts in team_stats():
            #print(ts)
        for t in teams:
            #for k, v in strength.items():
            if x == 2:
                print('\n')
                x = 0
            elif t in ts:
                t_sos = float(ts[t]) + float(strength[t])
                print(t, ts[t], t_sos)
                x += 1

        '''print(teams[x], ts[teams[x]])
        print(teams[y], ts[teams[y]])
        print('\n')
        x += 2
        y += 2
        '''
compare_stats()
            
