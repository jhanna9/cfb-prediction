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

# link to sos and streak
str_sched = 'https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other'
streak = 'https://www.teamrankings.com/ncf/standings/'

def sos(link):
    # dictionary to return
    str_sched = {}

    # pull data from site and create BS object
    strength = requests.get(link, headers=headers)
    soup = BeautifulSoup(strength.content)

    # iterate through BS object looking for td tag
    for tag in soup('td'):
        print tag.string

    return str_sched

sos(str_sched)
