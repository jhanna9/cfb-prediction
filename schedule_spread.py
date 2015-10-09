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
link_path = 'http://www.vegasinsider.com/college-football/odds/las-vegas/'

def schedule(link):
    games = []
    sched = requests.get(link, headers=headers)

    soup = BeautifulSoup(sched.content)
   
    for tag in soup('b'): #find_all(re.compile('b')):
        print tag.string

    return games

print schedule(link_path)


# spread = requests.get(link, headers=headers)
