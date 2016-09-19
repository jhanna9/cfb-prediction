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
    teams_new = []
    team_var = build_dict('team_variation.txt')

    for t in teams:
        for k, v in team_var.items():
            if t in v:
                teams_new.append(k)
            else:
                #print(t, 'did not match', k)
                pass
    print(len(teams_new))
            
    return teams_new

print(match_team())
#match_team()
