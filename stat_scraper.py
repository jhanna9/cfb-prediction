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

#list to store key stats
key_stats = ['Total Offense', 'Scoring Offense', '3rd Down Conversion Pct', 'Total Defense', 'Scoring Defense', '3rd Down Conversion Pct Defense']


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
     
    print data_lst[1]
    print data_lst[11]       
    
    file = open(stat + '_stats.txt', 'w')
        
    for head in header_lst:
        file.write(head + ' ')
    
    file.write('\n')

    x = 0
    y = len(header_lst)
    
    while x < len(data_lst):
        for data in data_lst:    
            if x == len(data_lst):
                break
            elif x < y:
                file.write(data_lst[x] + ' ')           
                x += 1
            else:
                file.write('\n')
                y += len(header_lst)

    file.close
         
# function calls
for key in key_stats:
    bs_objects(key) # loops key stats list and writes stats to file
