# a script to create links to and store statistics of ncaa football teams
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

# generic link that the stat code is attached to
x = raw_input("Enter 'ranking_period' for up-to-date stats(ie current period = 23.0. Add 3 per week for current stats): ") 
link = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=' + str(x) + '&amp;sport_code=MFB&amp;stat_seq='

# dictionary to store individual stats links
stat_link = {}

#list to store key stats
key_stats = ['Total Offense', 'Total Defense', 'Rushing Offense', 'Rushing Defense', 'Passing Offense', 'Passing Yards Allowed', 'Scoring Offense', 'Scoring Defense', 'Team Passing Efficiency', 'Team Passing Efficiency Defense', '3rd Down Conversion Pct', '3rd Down Conversion Pct Defense', 'Red Zone Offense', 'Red Zone Defense', 'Turnovers Lost', 'Turnovers Gained', 'Tackles for Loss Allowed', 'Team Tackles for Loss', 'Sacks Allowed', 'Team Sacks']

# build stat links
stat_link = build_link(f, link)


def stat_header(stat):
    '''Creates a Beautiful Soup object from stat parameter of stat page header

    Keyword arguments:
    stat - the statistic to be analyzed
    
    returns: a dictionary


    '''
    link = stat_link[stat]
    statistic = requests.get(link, headers=headers)

    soup = BeautifulSoup(statistic.content)

    secondtable = soup.find_all('table')[1]

    # list and dictionary
    header_lst = [stat]
    stat_head = {}
   
    for tag in secondtable.find_all(re.compile('th')):
        header_lst.append(tag.string)

    del header_lst[2]

    stat_head[header_lst[0]] = header_lst[1:]
            
    return stat_head



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
        tm_stat[data_lst[y]] = data_lst_chunk[x]
        x += 1
        y += len(header_lst)        

    return tm_stat
         
# function calls
for stats in key_stats:
    stat_dict_build(stats)
    print '\n'
    print '\n'

