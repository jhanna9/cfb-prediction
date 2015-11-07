# a script that compares stats and picks winners ats
# imports
import numpy
from schedule_spread import *
from sos import sos
from stat_scraper import *

# link to sos
str_sched = 'https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other'

#list to store key stats
key_stats = ['Total Offense', 'Total Defense', 'Rushing Offense', 'Rushing Defense', 'Passing Offense', 'Passing Yards Allowed', 'Scoring Offense', 'Scoring Defense', 'Team Passing Efficiency', 'Team Passing Efficiency Defense', '3rd Down Conversion Pct', '3rd Down Conversion Pct Defense', 'Red Zone Offense', 'Red Zone Defense', 'Turnovers Lost', 'Turnovers Gained', 'Tackles for Loss Allowed', 'Team Tackles for Loss', 'Sacks Allowed', 'Team Sacks']


#calculate the average of sos
def sos_avg(dict):

    avg = []

    for k, v in dict.iteritems():
        avg.append(v)

    x = 0

    for s in avg:
        x = x + float(s)

    average = x / len(avg)
    
    return average


def stand_dev(dict):

    stan_dev = []

    for k, v in dict.iteritems():
        stan_dev.append(float(v))

    std = numpy.std(stan_dev, axis=0)
    
    return std
    
    


# function calls
print stand_dev(sos(str_sched))
print '\n'

for s in key_stats:
    print round(stand_dev(stat_dict_build(s)), 2)
    print '\n'
    

