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
streak = 'https://www.teamrankings.com/ncf/standings/'

def sos(link):
    # dictionary to return
    str_sched = {}

    # list for storage
    sos_lst = []
    #sos_stor = []
    #team_stor = []
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
    

    '''x = 1

    while x < len(team_stor):
        team_lst.append(team_stor[x])
        x += 2

    y = 2

    while sos_stor[y] != '40':
        sos_lst.append(sos_stor[y])
        y += 6

    '''

    # create dictionary of game team as the key and strenght of schedule as the value
    str_sched = dict(zip(team_lst, sos_lst))
  

    return str_sched

for k, v in sos(str_sched).iteritems():
    print k, v
