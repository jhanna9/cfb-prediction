# a script to scrape the schedule and spread of ncaa football teams from covers
# imports
import re
import requests
import sys
from bs4 import BeautifulSoup

# defaults encoding to utf-8
reload(sys)
sys.setdefaultencoding("utf-8")

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# link to sos and streak
str_sched = 'https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other'
wl_strk = 'http://www.ncaa.com/standings/football/fbs'

def sos(link):
    # dictionary to return
    str_sched = {}

    # list for storage
    sos_lst = []
    team_lst = []

    # pull data from site and create BS object
    strength = requests.get(link, headers=headers)
    soup = BeautifulSoup(strength.content)
    table = soup.find_all('table')[0]

    # iterate through BS object looking for a and td tags
    for tag in table.find_all(re.compile('a')):
        team_lst.append(tag.string)   

    for tag in soup('td'):
        sos_lst.append(tag.string)

    # slice lists to get proper data
    team_lst = team_lst[1::2]
    sos_lst = sos_lst[2::6]

    # create dictionary of game team as the key and strenght of schedule as the value
    str_sched = dict(zip(team_lst, sos_lst))
  
    return str_sched


def streak(link):
    # dictionary to return
    strk_lst = {}

    # list for storage
    strk_lst = []
    team_lst = []

    # pull data from site and create BS object
    win_streak = requests.get(link, headers=headers)
    soup = BeautifulSoup(win_streak.content)
    # table = soup.find_all('table')

    # iterate through BS object looking for a and td tags
    for tag in soup('a'):
        team_lst.append(tag.string)   

    for tag in soup('td'):
        strk_lst.append(tag.string)

    # slice lists to get proper data
    team_lst = team_lst[117:245]
    strk_lst = strk_lst[7::8]

    for s in strk_lst:
        if s == 'STREAK':
            strk_lst.remove(s)    

    # create dictionary of game team as the key and strenght of schedule as the value
    strk_lst = dict(zip(team_lst, strk_lst))
  
    return strk_lst

#calculate the average strength of schedule
def sos_avg(sos_dict):

    avg = []

    for k, v in sos_dict.iteritems():
        avg.append(v)

    x = 0

    for s in avg:
        x = x + float(s)

    average = x / len(avg)
    
    print average

    return average


def sos_weight(t1, t2, avg):
    '''Creates the weighted sos number to add/subtract to the team's scores 

    Keyword arguments:
    t1 - the sos number from a team
    t2 - the sos number from a second team
    avg - sos average calculated by sos_avg()
    
    returns: a float


    '''
    if t1 >= 0 and t2 >= 0:
        weight = (abs((t1 - t2) / avg) / 10) / 2
    elif t1 <= 0 and t2 >= 0:
        weight = abs(((t1 + t2) / avg) / 10) / 2
    elif t1 >= 0 and t2 <= 0:
        weight = abs(((t1 + t2) / avg) / 10) / 2
    elif t1 <= 0 and t2 <= 0:
        weight = abs(((t1 - t2) / avg) / 10) / 2

    return weight
    

# function calls
#for k, v in sos(str_sched).iteritems():
    #print k, v
#for k, v in streak(wl_strk).iteritems():
    #print k, v
print sos_weight(10.9, 9.7, sos_avg(sos(str_sched)))

