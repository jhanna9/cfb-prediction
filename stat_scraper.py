# a script to create links to and store statistics of ncaa football teams
# imports
import csv
import re
import sys
from bs4 import BeautifulSoup
from link_builder import build_link
from urllib import urlopen

# defaults encoding to utf-8
reload(sys)
sys.setdefaultencoding("utf-8")

# file that contains numeric code for each stat 
f = open('stat_value.txt', 'r')
link = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq='

# dictionary to store individual stats links
stat_link = {}

stat_link = build_link(f, link)

for k, v in stat_link.iteritems():
    print 'stat: ', k + '\n'
    print 'link: ', v + '\n\n'


def bs_objects(stat):
    '''Creates a Beautiful Soup object from stat parameter and writes it to a file

    Keyword arguments:
    stat - the statistic to be analyzed
    
    returns: a file


    '''
    link = stat_link[stat]
    statistic = urlopen(link)

    soup = BeautifulSoup(statistic)
    
    file = open('team_stats.txt', 'w')
    file.write(soup.prettify(formatter="html"))
    file.close

# function calls
# stat_value_dict(f)
# build_link()
# bs_objects('Total Defense') # writes Beautiful Souped Total Defense stat page to file 
# bs_objects('Scoring Defense') # writes Beautiful Souped Scoring Defense stat page to file


'''function tests

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


