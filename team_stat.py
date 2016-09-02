from links import build_stat_dict
from schedule_spread import schedule
from soup import soupy

def team_stat_dict():
    '''

    '''

    # link to schedule and spread
    data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

    teams = schedule(data)
    print(teams)

    # builds then iterates through each stat's BS obj
    for k in build_stat_dict('stat_position.txt').items():
        # creates a BS object per stat
        stats = soupy(k)

team_stat_dict()    
