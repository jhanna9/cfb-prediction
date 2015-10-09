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
    sched = requests.get(link, headers=headers)

    soup = BeautifulSoup(sched.content)
    
    #info = soup.find_all('b')
    
    for line in soup:
        '''match = re.search(r'>([\w\s])+<', line, re.IGNORECASE)
        if match:
            print match.group(1)
            # stat_link[match.group(2)] = path + match.group(1)
        else:
            print False
        '''
        for tag in soup.find_all(re.compile('b')):
            if tag == False:
                pass
            else:
                print tag

    # return info

schedule(link_path)


# spread = requests.get(link, headers=headers)
