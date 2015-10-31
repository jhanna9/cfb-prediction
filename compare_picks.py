# a script that compares stats and picks winners ats
# imports
import re
import requests
import sys
from bs4 import BeautifulSoup
from link_builder import build_link

# defaults encoding to utf-8
reload(sys)
sys.setdefaultencoding("utf-8")

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# links
data = 'http://www.covers.com/odds/football/college-football-odds.aspx'
str_sched = 'https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other'
x = raw_input("Enter 'ranking_period' for up-to-date stats(ie current period = 28.0. Add 3 per week for current stats): ")
# generic link that the stat code is attached to 
link = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=' + str(x) + '&amp;sport_code=MFB&amp;stat_seq=' 

# file that contains numeric code for each stat 
f = open('stat_value.txt', 'r')

# dictionary to store individual stats links
stat_link = {}

#list to store key stats
key_stats = ['Total Offense', 'Total Defense', 'Rushing Offense', 'Rushing Defense', 'Passing Offense', 'Passing Yards Allowed', 'Scoring Offense', 'Scoring Defense', 'Team Passing Efficiency', 'Team Passing Efficiency Defense', '3rd Down Conversion Pct', '3rd Down Conversion Pct Defense', 'Red Zone Offense', 'Red Zone Defense', 'Turnovers Lost', 'Turnovers Gained', 'Tackles for Loss Allowed', 'Team Tackles for Loss', 'Sacks Allowed', 'Team Sacks']

# build stat links
stat_link = build_link(f, link)


def stat_dict_build(stat):
    '''Creates a Beautiful Soup object from stat parameter of each stat 

    Keyword arguments:
    stat - the statistic to be analyzed
    
    returns: a dictionary


    '''
    link = stat_link[stat]
    statistic = requests.get(link, headers=headers)

    soup = BeautifulSoup(statistic.content)

    secondtable = soup.find_all('table')[1]
    
    # lists and dictionaries
    header_lst = [stat]
    data_lst = []
    stat_head = {}
    tm_stat = {}
   
    for tag in secondtable.find_all(re.compile('th')):
        header_lst.append(tag.string)

    for tag in secondtable.find_all(re.compile('td')):        
        data_lst.append(tag.string.strip())

    for x in data_lst:
        if x =='Reclassifying':
            data_lst.remove(x)

    del header_lst[2]

    # creates chunks of data by team and stat based on length of header_lst
    data_lst_chunk = [data_lst[x:x + len(header_lst)] for x in xrange(0, len(data_lst), len(header_lst))]
    
    x = 0
    y = 1

    # create tm_stat dict with team as key and stats as value
    while x < len(data_lst_chunk):
        del data_lst_chunk[x][1]
        tm_stat[data_lst[y]] = data_lst_chunk[x][-1]
        x += 1
        y += len(header_lst)        

    return tm_stat
    

def combo_stats():
    '''Creates a dictionary with team as key and key stats as value 

    Keyword arguments:
    stats_dict - stats dictionaries to be combined into a single dictionary 
    
    returns: a dictionary


    '''
    combo = []
    combo_all = {}

    for s in key_stats:
        combo.append(stat_dict_build(s))

    for k in combo[0].iterkeys():
        combo_all[k] = tuple(combo_all[k] for combo_all in combo)

    return combo_all


def schedule(link):
    '''Takes a URL input and scrapes for team names

    Keyword arguments:
    link -- url to game schedule

    returns: a list


    '''
    # list to return
    games = []
    
    # pull data from site and create BS object
    sched = requests.get(link, headers=headers)
    soup = BeautifulSoup(sched.content)

    # iterate through BS object looking for strong tag
    for tag in soup('strong'):
        games.append(tag.string)

    return games


def spread(link):
    '''Takes a URL input and scrapes for current spread

    Keyword arguments:
    link -- url to game schedule

    returns: a list


    '''
    # list to return
    spread_lst = []
    
    # pull data from site and create BS object
    spread = requests.get(link, headers=headers)
    soup = BeautifulSoup(spread.content)

    # iterate through BS object looking for div and class='covers_bottom'
    for tag in soup.find_all('div', class_='covers_bottom'):
        spread_lst.append(tag.string.strip())

    return spread_lst 
   
    
def match_spread(sched, spread):
    '''Takes two objects that return lists

    Keyword arguments:
    sched -- schedule function called with URL
    spread -- spread function called with URL

    returns: a dictionary


    '''
    # dictionary to return and a placeholder list
    matchup_spread = {}
    matchup = []

    # variables
    x = 0
    y = 1

    # create a list with game matchups
    while x < len(sched):
        matchup.append(sched[x] + ' vs. ' + sched[y])
        x += 2
        y += 2  
    
    # create dictionary of game matchups as the key and spreads as the value
    matchup_spread = dict(zip(matchup, spread))

    return matchup_spread


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


#calculate the average strength of schedule
def sos_avg(sos_dict):

    avg = []

    for k, v in sos_dict.iteritems():
        avg.append(v)

    x = 0

    for s in avg:
        x = x + float(s)

    average = x / len(avg)
    
    #print average

    return average

#calculate weighted sos score
def sos_weight(t1, t2, avg):
    '''Creates the weighted sos number to add/subtract to the team's scores 

    Keyword arguments:
    t1 - the sos number from a team
    t2 - the sos number from a second team
    avg - sos average calculated by sos_avg()
    
    returns: a float


    '''
    weight = round((abs((t1 - t2) / avg) / 10) / 2, 4)

    return weight

for k, v in combo_stats().iteritems():
    print k, v
    print '\n'
