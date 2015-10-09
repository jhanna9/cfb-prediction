# a script to scrape the schedule and spread of ncaa football teams from vegas insider/mirage sportsbook
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

# links to schedule and spread
link_sched = 'http://www.vegasinsider.com/college-football/odds/las-vegas/'
link_spread = 'http://www.vegas.com/gaming/sportsline/college-football/'

# global list
# games = []

def schedule(link):
    games = []
    sched = requests.get(link, headers=headers)

    soup = BeautifulSoup(sched.content)
   
    for tag in soup('b'):
        games.append(tag.string)

    return games[:-3]


def spread(link):
    tabledata_lst = []
    spread_lst = []  
    
    spread = requests.get(link, headers=headers)

    soup = BeautifulSoup(spread.content)

    tabledata = soup.find_all('td')

    for tag in tabledata:
        tabledata_lst.append(tag.string)
        
    x = 35

    while x < len(tabledata_lst):
        spread_lst.append(tabledata_lst[x])
        x += 45

    return spread_lst


def match_spread(sched, spread):
    # Prints the schedule in format: 'Team 1 vs. Team 2'
    matchup_spread = {}
    matchup = []

    x = 0
    y = 1

    while x < len(sched):
        matchup.append(sched[x] + ' vs. ' + sched[y])
        x += 2
        y += 2  
    
    matchup_spread = dict(zip(matchup, spread))

    return matchup_spread


# function calls
print match_spread(schedule(link_sched), spread(link_spread))
#print schedule(link_sched)
#print spread(link_spread)



