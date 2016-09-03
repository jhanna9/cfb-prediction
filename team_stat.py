from links import build_stat_dict
from schedule_spread import schedule
from soup import soupy

def team_stat_dict():
    '''

    '''

    # dictionary to hold teams and stats
    team_stat = {}

    # link to schedule and spread
    data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

    teams = schedule(data)

    # builds then iterates through each stat's BS obj
    for k, v in build_stat_dict('stat_position.txt').items():
        # creates a BS object per stat
        stats = soupy(k)
        print(k)

        for t in teams:  
            if t in stats:
                #print(t + ' is in stats list' + '\n')
                p = stats.index(t)
                print(p)
                #print(stats[int(p) + (int(v) - 2)])
                team_stat[t] = stats[int(p) + (int(v) - 2)]
            else:
                #print(t + ' is not in stats list' + '\n')
                pass
        
    return team_stat
            
print(team_stat_dict())
