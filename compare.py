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
    x = 0
    y = 0
    home_team = ''
    away_team = ''
    ht_score = 0
    at_score = 0
    fin = 0
        
    # use this loop for comparison
    for t in teams:
        if y == 0:
            away_team = t       
        elif x == 1:
            home_team = t
            at_score = sum(team_score)                

        team_score = []             

        for ts in team_stats(): # ts is dict with team: zscore per stat
            if x == 2:
                
                print(at_score)
                print(ht_score) 
                fin = abs(at_score - ht_score)

                print(away_team, '@', home_team)
                if at_score > ht_score:
                    print(away_team, 'gets', round(fin, 2), 'points.')
                    x = 0
                else:
                    print(home_team, 'gets', round(fin, 2), 'points.')
                    x = 0
                print('\n')
                              
            # if team is in ts dict
            elif t in ts:
                # ts[t] = key call to get value of team in ts / strength[t] = s.o.s. zscore for team
                t_sos = float(ts[t]) + float(strength[t]) 
                #print(t, ts[t], strength[t], round(t_sos, 2))
                team_score.append(t_sos)                                              
            else:
                print(t, 'has not intercepted a pass this season.')

        ht_score = sum(team_score)
        x += 1                   
        
        #print(t, round(sum(team_score),2), len(team_score))    

compare_stats()         
