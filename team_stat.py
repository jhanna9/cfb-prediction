from links import build_dict
import re
from schedule_spread import schedule
from soup import soupy

def team_stat_dict():
    '''

    '''

    # builds then iterates through each stat's BS obj
    for k, v in build_dict('stat_position.txt').items():
        # list to hold teams and stats
        team_lst = []
        stat_lst = []

        # creates a BS object per stat
        stats = soupy(k)
        print('\n')
        print(k)
        print('\n')
        '''print(stats)
        print('\n')
        print('\n')
        '''
        
        # position of each important number within BS object list
        x = int(v)
        a = 1
        b = 2
        
        # variables to find the next important number
        y = x + 1
        z = x + 3
        c = 6

        # iterates through BS object to append important num to list
        for s in stats:
            if x > len(stats):
                break
            else:
                if k == 'Strength_Schedule':
                    for t in stats:
                        search_str = stats[a]

                        team_match = re.search(r'^[a-zA-Z]+-*\s*[a-zA-Z]*\s*[a-zA-Z]*', search_str)

                        if team_match == None:
                            break
                        else:
                            team_lst.append(team_match.group())
                            stat_lst.append(stats[b])
                            a += c
                            b += c
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
        
    return team_lst, stat_lst 
            
print(team_stat_dict())
