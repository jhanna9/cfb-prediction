import re
import requests
from bs4 import BeautifulSoup
from scipy import stats

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
    soup = BeautifulSoup(site.content, 'html.parser')
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


def z_score(t_lst, s_lst):
    score = []
    stat = []
    team = []

    team = t_lst
    stat = s_lst

    for s in stat:
        score.append(float(s))
              
    score = ['%.2f' % s for s in stats.zscore(score)] 

    tm_zscore = dict(zip(team, score))

    return tm_zscore
    
