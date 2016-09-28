from links import build_dict
from schedule_spread import schedule
from sos_2016 import sos, zscore
from team_stat import team_stats

def match_team(teams):
    '''

    '''
    # builds dictionary of variation on team names
    team_var = build_dict('team_variation.txt')
    
    # list to return and list to place hold teams not in team_var
    teams_new = []
    no_list = []
    
    # iterates through teams and team_var
    x = 0

    for t in teams:
        if len(teams) == 128:
            for k, v in team_var.items():
                if t in v:
                    teams_new.append(k)
        else:
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
    #print(teams)
    #print(len(teams))
    strength = zscore(match_team(sos()[0]), sos()[1]) # z score for s.o.s.
    #print(len(match_team(sos()[0])))
    #print(match_team(sos()[0]))
    x = 0
        
    # use this loop for comparison
    for ts in team_stats(): # ts is dict with team: zscore per stat
        for t in teams:
            #if x == 2:
                #print('\n')
                #x = 0
            # if team is in ts dict
            if t in ts:
                # ts[t] = key call to get value of team in ts / strength[t] = s.o.s. zscore for team
                t_sos = float(ts[t]) + float(strength[t]) 
                print(t, ts[t], round(t_sos, 2))
                x += 1
            else:
                print(t, 'not in teams')

compare_stats()         
