import requests
from bs4 import BeautifulSoup
import re

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}


def soupy():
    '''Loops through the statistic links to create a BeautifulSoup Object

       Keyword Argument:
       stat -- the statistic used to build links

       returns a list
    '''

    # get site info using requests
    site = requests.get('https://www.teamrankings.com/college-football/ranking/schedule-strength-by-other', headers=headers) 

    # create BS object, sort through necessary info
    soup = BeautifulSoup(site.content)
    team = soup.find_all('td')

    team_lst = []
    stat_lst = []

    h = 1
    i = 2
    j = 6
    for t in team:
            str = team[h].get_text()

            team_match = re.search(r'^[a-zA-Z]+-*\s*[a-zA-Z]*\s*[a-zA-Z]*', str)

            if team_match == None:
                break
            else:
                team_lst.append(team_match.group())
                stat_lst.append(team[i].get_text())
                h += j
                i += j

    return team_lst, stat_lst

    '''x = 11
    while x <= len(team):
        print(team[x].get_text())
        x += 10
    '''

print(soupy())
