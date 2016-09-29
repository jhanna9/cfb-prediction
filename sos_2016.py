import requests
from bs4 import BeautifulSoup
import re
from standard_score import z_score

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}


def sos():
    '''Loops through the statistic links to create a BeautifulSoup Object

       Keyword Argument:
       stat -- the statistic used to build links

       returns a dictionary
    '''
    # get site info using requests
    site = requests.get('https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other', headers=headers) 

    # create BS object, sort through necessary info
    soup = BeautifulSoup(site.content)
    team = soup.find_all('td')

    team_lst = []
    stat_lst = []

    x = 1
    y = 2
    z = 6
    for t in team:
        team_str = team[x].get_text()

        team_match = re.search(r'([&\w\s*-]+)([(\w\w)]+)', team_str)

        if len(stat_lst) == 128:
            break
        elif team_match.group(1) == 'Miami ':
            whole_miami = team_match.group(1) + team_match.group(2).strip()
            team_lst.append(whole_miami)
            stat_lst.append(team[y].get_text())
            x += z
            y += z
        else:
            team_lst.append(team_match.group(1).strip())
            stat_lst.append(team[y].get_text())
            x += z
            y += z

    return team_lst, stat_lst


def zscore(team, stat):
    '''

    '''
    stand_score = z_score(team, stat)

    return stand_score
    
