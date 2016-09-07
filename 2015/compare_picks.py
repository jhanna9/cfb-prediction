# a script that compares stats and picks winners ats
# imports
import numpy
from schedule_spread import *
from scipy import stats
from sos import sos
from stat_scraper import *

# link to sos, schedule, and spread
str_sched = 'https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other'
data = 'http://www.covers.com/odds/football/college-football-odds.aspx'

#list to store key stats
key_stats = ['Total Offense', 'Total Defense', 'Rushing Offense', 'Rushing Defense', 'Passing Offense', 'Passing Yards Allowed', 'Scoring Offense', 'Scoring Defense', 'Team Passing Efficiency', 'Team Passing Efficiency Defense', '3rd Down Conversion Pct', '3rd Down Conversion Pct Defense', 'Red Zone Offense', 'Red Zone Defense', 'Turnovers Lost', 'Turnovers Gained', 'Tackles for Loss Allowed', 'Team Tackles for Loss', 'Sacks Allowed', 'Team Sacks']

x = 0

for t in schedule(data):
    for k, v in combo_stats().iteritems():    
        if t == k and x % 1:
            print k, v
            print '\n'    


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

    stdev = numpy.std(stan_dev, axis=0)
    
    return stdev

def z_score(dic):
    score = []
    team = []
    
    for k, v in dic.iteritems():
        team.append(k)
        score.append(float(v))

    score = stats.zscore(score)

    score2 = ['%.2f' % elem for elem in score]

    tm_zscore = dict(zip(team, score2))

    return tm_zscore
    

def stat_std_lst():
    std_lst = []

    for s in key_stats:
        std_lst.append(round(stand_dev(stat_dict_build(s)), 2))

    return std_lst 


def compare(tm_stat, tm_sos):

    pass

    
    
             
# function calls      
'''
#z_score(sos(str_sched))
for k, v in z_score(sos(str_sched)).iteritems():
    print k, v
    print '\n'

print sos_avg(sos(str_sched))
print stand_dev(sos(str_sched))

# print std_range(sos_avg(sos(str_sched)), stand_dev(sos(str_sched))) 

# print stat_std_lst()

#compare(combo_stats(), sos(str_sched))

# possibly unnecessary functions

def std_range(avg, std_sos):
    
    sdev_pos = []
    sdev_neg = []
        
    x = 0
    y = 1

    while x < 3:
        sdev_pos.append(avg + (std_sos * y))
        sdev_neg.append(avg - (std_sos * y))
        x += 1
        y += 1

    sdev_neg.append(avg)
    
    sdev_all =  sdev_neg + sdev_pos

    sdev_all_2 = ['%.2f' % elem for elem in sdev_all]

    return sdev_all_2

'''





    

