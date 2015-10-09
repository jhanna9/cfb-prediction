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
link_path = 'http://www.vegasinsider.com/college-football/odds/las-vegas/'

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
    spread = requests.get(link, headers=headers)

    soup = BeautifulSoup(spread.content)

    tabledata = soup.find_all('td')

    x = 0
    y = 27

    while x < 4:
        print tabledata[y]
        x += 1
        y += 12
        
    #for tag in tabledata:
        #print tag

# function calls
#print schedule(link_path)
spread(link_path)



