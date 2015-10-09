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

def schedule(link):
    games = []
    sched = requests.get(link, headers=headers)

    soup = BeautifulSoup(sched.content)
   
    for tag in soup(''):
        games.append(tag.string)

    '''Prints the schedule in format: 'Team 1 vs. Team 2'
    x = 0
    y = 1
    games = games[:-3]

    while x < len(games):
        print games[x] + ' vs. ' + games[y]
        x += 2
        y += 2
    '''

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

    print len(spread_lst)
    print spread_lst[49]
    print spread_lst[50]
    print spread_lst[51]
    print spread_lst[52]

    return spread_lst


# function calls
#print schedule(link_sched)
spread(link_spread)



