from links import build_dict
from schedule_spread import schedule
from soup import soupy

def team_stat_dict():
    '''

    '''

    # dictionary to hold teams and stats
    team_stat = {}

    # builds then iterates through each stat's BS obj
    for k, v in build_dict('stat_position.txt').items():

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
        
        # variables to find the next important number
        y = x + 1
        z = x + 3

        # iterates through BS object to append important num to list
        for s in stats:
            if x > len(stats):
                break
            else:
                if k == 'Passes_Intercepted':
                    team_stat[stats[a]] = stats[x]
                    x += z
                    a += z
                else:
                    team_stat[stats[a]] = stats[x]
                    x += y
                    a += y
        print(team_stat)
        
    return team_stat
            
team_stat_dict()
