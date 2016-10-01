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
    strength = zscore(match_team(sos()[0]), sos()[1]) # z score for s.o.s.
    team_score = []
    tz = []
    fin = 0
        
    # use this loop for comparison
    for t in teams:
        if len(team_score) == 0:
            tz.append(t)
        elif len(tz) == 4:
                fin = abs(tz[1] - tz[3])

                print(tz[0], '@', tz[2])

                if tz[1] > tz[3]:
                    print(tz[0], 'gets', round(fin, 2), 'points.')
                    tz = []
                    tz.append(t)
                else:
                    print(tz[2], 'gets', round(fin, 2), 'points.')
                    tz = []
                    tz.append(t)
                print('\n')
        else:        
            tz.append(t)
            

        team_score = []             

        for ts in team_stats(): # ts is dict with team: zscore per stat            
            
                              
            # if team is in ts dict
            if t in ts:
                # ts[t] = key call to get value of team in ts / strength[t] = s.o.s. zscore for team
                t_sos = float(ts[t]) + float(strength[t])
                team_score.append(t_sos)                                              
            else:
                print(t, 'has not intercepted a pass this season.')
        
        tz.append(sum(team_score))                  
        
        #print(t, round(sum(team_score),2), len(team_score))    

compare_stats()         
