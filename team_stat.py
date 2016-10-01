from links import build_dict
import re
from schedule_spread import schedule
from standard_score import z_score
from soup import soupy


def team_stats():
    '''

    '''

    # builds then iterates through each stat's BS obj
    for k, v in build_dict('stat_position.txt').items():
        
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

        yield stand_score

# use this loop for comparison
#for ts in team_stats():
    #print(len(ts))
