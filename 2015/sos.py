import re
import requests
from bs4 import BeautifulSoup

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

def sos():
    '''Scrapes strength of schedule/team from teamrankings

        returns a dictionary
    '''
    
    # link to sos
    link = 'https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other'

    # dictionary to return
    str_sched = {}

    # list for storage
    sos_lst = []
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

    # create dictionary of game team as the key and strenght of schedule as the value
    str_sched = dict(zip(team_lst, sos_lst))
  
    return str_sched

# function calls
#for k, v in sos().items():
    #print(k, v)
