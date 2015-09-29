import re
import sys
from urllib import urlopen
from bs4 import BeautifulSoup

reload(sys)
sys.setdefaultencoding("utf-8")
 
f = open('stat_value.txt', 'r')
stat_value = {}
stat_link = {}

def stat_value_dict(filename):
    for line in filename:
        match = re.search(r'([\d]+).0">([\w\s]+)', line, re.IGNORECASE)
        if match:
            stat_value[match.group(2)] = match.group(1)
        else:
            print False
    
    return stat_value

def build_link():
    link = 'stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq='
    for key, value in stat_value.iteritems():
        stat_link[key] = link + value

    return stat_link
                 
            
stat_value_dict(f)
build_link()

'''test for functions

for key, value in stat_link.iteritems():
    print key, value

print stat_value['Total Defense']
print stat_value['Fewest Penalty Yards Per Game']

'''

third_down_durl = 'http://stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq=22.0'
third_down_dpage = urlopen(third_down_durl)

soup = BeautifulSoup(third_down_dpage)

# print soup.find_all('table')

'''link to stats only page:


stats.ncaa.org/rankings/national_ranking?academic_year=2016.0&amp;division=11.0&amp;ranking_period=14.0&amp;sport_code=MFB&amp;stat_seq=


'''
