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

# link to schedule and spread
data = 'http://www.covers.com/odds/football/college-football-odds.aspx'


def schedule(link):
    games = []
    sched = requests.get(link, headers=headers)
    soup = BeautifulSoup(sched.content)

    for tag in soup('strong'):
        games.append(tag.string)

    return games


def spread(link):
    spread_lst = []
    spread = requests.get(link, headers=headers)
    soup = BeautifulSoup(spread.content)

    for tag in soup.find_all('div', class_='covers_bottom'):
        spread_lst.append(tag.string.strip())

    return spread_lst 
   
    
def match_spread(sched, spread):
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
print match_spread(schedule(data), spread(data))




