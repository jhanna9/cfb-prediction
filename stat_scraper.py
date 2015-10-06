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
x = raw_input("Enter 'ranking_period' for up-to-date stats(ie current period = 17.0. Add 3 per week for current stats): ") 
link = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=' + str(x) + '&amp;sport_code=MFB&amp;stat_seq='

# dictionary to store individual stats links
stat_link = {}

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
    
    header_lst = []
    data_lst = []
   
    for tag in secondtable.find_all(re.compile('th')):
        header_lst.append(tag.string)

    for tag in secondtable.find_all(re.compile('td')):        
        data_lst.append(tag.string.strip())
            
    
    file = open('team_stats.txt', 'w')
    
    for head in header_lst:
        file.write(head + ' ')

    file.write('\n')

    x = 0
    y = 10
    
    while x < len(data_lst):
        for data in data_lst:    
            if x == len(data_lst):
                break
            elif x < y:
                file.write(data_lst[x] + ' ')           
                x += 1
            else:
                file.write('\n')
                y += 10

    file.close
         
# function calls
bs_objects('Total Defense') # writes Beautiful Souped Total Defense stat page to file 
# bs_objects('Scoring Defense') # writes Beautiful Souped Scoring Defense stat page to file


'''function tests/old functions

for key, value in stat_link.iteritems():
    print "key: ", key + '\n'
    print "link: ", value + '\n\n'

print stat_value['Total Defense']
print stat_value['Fewest Penalty Yards Per Game']

third_down_durl = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq=22.0'
third_down_dpage = urlopen(third_down_durl)

soup = BeautifulSoup(third_down_dpage)

# print soup.find_all('table')

def stat_value_dict(filename):
    Pulls stat code from file and stores it in stat_value dictionary

    Keyword arguments:
    filename -- file used to store stat codes
    
    returns: a dictionary


    
    for line in filename:
        match = re.search(r'([\d]+).0">([\w\s]+)', line, re.IGNORECASE)
        if match:
            stat_value[match.group(2)] = match.group(1)
        else:
            print False
    
    return stat_value

def build_link():
Combines link and stat code to create stat specific link

    Keyword arguments:
    None
    
    returns: a dictionary


    
    
    for key, value in stat_value.iteritems():
        stat_link[key] = link + value

    return stat_link

'''


