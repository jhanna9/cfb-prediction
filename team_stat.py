from links import build_dict
import re
from schedule_spread import schedule
from sos_2016 import z_score
from soup import soupy


def team_stats():
    '''

    '''
    lower_better = [
                    '3rd_Down_Conversion_Pct_Defense',
                    '4th_Down_Conversion_Pct_Defense',
                    'Blocked_Kicks_Allowed',
                    'Blocked_Punts_Allowed',
                    'First_Downs_Defense',
                    'Fumbles_Lost',
                    'Kickoff_Return_Defense',  
                    'Total_Defense',
                    'Rushing_Defense',
                    'Passing_Yards_Allowed',
                    'Punt_Return_Defense',
                    'Scoring_Defense',
                    'Team_Passing_Efficiency_Defense',
                    'Red_Zone_Defense',
                    'Passes_Had_Intercepted',
                    'Tackles_for_Loss_Allowed',
                    'Sacks_Allowed',
                    'Turnovers_Lost'
                   ]

    # builds then iterates through each stat's BS obj
    for k, v in build_dict('stat_position_def.txt').items():
        
        # creates a BS object per stat
        stats = soupy(k)
        
        # position of each important number within BS object list
        x = int(v)
        a = 1
        b = 2
        
        # variables to find the next important number
        y = x + 1
        z = x + 3
        c = 6

        # list to hold teams and stats
        team_lst = []
        stat_lst = []

        # iterates through BS object to append important num to list
        for s in stats:
            if x > len(stats):
                break
            elif k == 'Passes_Intercepted':
                team_lst.append(stats[a])
                stat_lst.append(stats[x])
                x += z
                a += z
            else:
                team_lst.append(stats[a])
                stat_lst.append(stats[x])
                x += y
                a += y

        stand_score = z_score(team_lst, stat_lst)

        for key, val in stand_score.items():
            val = float(val)
            if k in lower_better:
                if val < 0:
                    stand_score[key] = abs(val)
                else:
                    stand_score[key] = (val - (val * 2))
            else:
                pass    
        
        yield stand_score

# use this loop for comparison
#for ts in team_stats():
    #print(len(ts))
