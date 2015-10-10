# a script to scrape the schedule and spread of ncaa football teams from covers
# imports
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
    '''Takes a URL input and scrapes for team names

    Keyword arguments:
    link -- url to game schedule

    returns: a list


    '''
    # list to return
    games = []
    
    # pull data from site and create BS object
    sched = requests.get(link, headers=headers)
    soup = BeautifulSoup(sched.content)

    # iterate through BS object looking for strong tag
    for tag in soup('strong'):
        games.append(tag.string)

    return games


def spread(link):
    '''Takes a URL input and scrapes for current spread

    Keyword arguments:
    link -- url to game schedule

    returns: a list


    '''
    # list to return
    spread_lst = []
    
    # pull data from site and create BS object
    spread = requests.get(link, headers=headers)
    soup = BeautifulSoup(spread.content)

    # iterate through BS object looking for div and class='covers_bottom'
    for tag in soup.find_all('div', class_='covers_bottom'):
        spread_lst.append(tag.string.strip())

    return spread_lst 
   
    
def match_spread(sched, spread):
    '''Takes two objects that return lists

    Keyword arguments:
    sched -- schedule function called with URL
    spread -- spread function called with URL

    returns: a dictionary


    '''
    # dictionary to return and a placeholder list
    matchup_spread = {}
    matchup = []

    # variables
    x = 0
    y = 1

    # create a list with game matchups
    while x < len(sched):
        matchup.append(sched[x] + ' vs. ' + sched[y])
        x += 2
        y += 2  
    
    # create dictionary of game matchups as the key and spreads as the value
    matchup_spread = dict(zip(matchup, spread))

    return matchup_spread


# function calls
print match_spread(schedule(data), spread(data))




