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

            team_match = re.search(r'([\w\s-]+)([\w\s&()]*)', team_str)  #r'^[a-zA-Z]-*\s*[a-zA-Z]*\s*[a-zA-Z]*', str)
            print(team_match.group())
            #print(team_match.group(2))

            if team_match == None:
                break
            else:
                team_lst.append(team_match.group())
                stat_lst.append(team[y].get_text())
                x += z
                y += z

    return team_lst, stat_lst

print(sos()[0])


def zscore(team, stat):
    '''

    '''
    stand_score = z_score(team, stat)

    return stand_score
    
