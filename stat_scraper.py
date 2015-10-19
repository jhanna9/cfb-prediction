# a script to create links to and store statistics of ncaa football teams
# imports
import csv
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

# file that contains numeric code for each stat 
f = open('stat_value.txt', 'r')

# generic link that the stat code is attached to
x = raw_input("Enter 'ranking_period' for up-to-date stats(ie current period = 23.0. Add 3 per week for current stats): ") 
link = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=' + str(x) + '&amp;sport_code=MFB&amp;stat_seq='

# dictionary to store individual stats links
stat_link = {}

#list to store key stats
key_stats_off = ['Total Offense', 'Rushing Offense', 'Passing Offense', 'Scoring Offense', 'Team Passing Efficiency', '3rd Down Conversion Pct', 'Red Zone Offense', 'Turnovers Lost', 'Tackles for Loss Allowed', 'Sacks Allowed']
key_stats_def = ['Total Defense', 'Rushing Defense', 'Passing Yards Allowed', 'Scoring Defense', 'Team Passing Efficiency Defense', '3rd Down Conversion Pct Defense', 'Red Zone Defense', 'Turnovers Gained', 'Team Tackles for Loss', 'Team Sacks']


# build stat links
stat_link = build_link(f, link)

def bs_objects(stat):
    '''Creates a Beautiful Soup object from stat parameter and writes it to a file

    Keyword arguments:
    stat - the statistic to be analyzed
    
    returns: a file


    '''
    link = stat_link[stat]
    statistic = requests.get(link, headers=headers)

    soup = BeautifulSoup(statistic.content)

    secondtable = soup.find_all('table')[1]

    header_lst = [stat]
    data_lst = []

    # dictionaries
    stat_head = {}
    tm_stat = {}
   
    for tag in secondtable.find_all(re.compile('th')):
        header_lst.append(tag.string)

    for tag in secondtable.find_all(re.compile('td')):        
        data_lst.append(tag.string.strip())

    for x in data_lst:
        if x =='Reclassifying':
            data_lst.remove(x)

    stat_head[header_lst[0]] = header_lst[1:]

    #data_lst = data_lst[0::11]    

    #tm_stat[data_lst[0]] = data_lst[1:]

    for k, v in stat_head.iteritems():
        print k, v

    #for k, v in tm_stat.iteritems():
        #print k, v
            
    return data_lst
         
# function calls
# for key in key_stats_off:
bs_objects('Total Offense') # loops key stats list and writes stats to file
