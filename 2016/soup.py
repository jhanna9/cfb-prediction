import requests
from bs4 import BeautifulSoup
from links import build_links

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}


def soupy(stat):
    '''Loops through the statistic links to create a BeautifulSoup Object

       Keyword Argument:
       stat -- the statistic used to build links

       returns a list
    '''

    # list to hold all teams and selected stat
    team_stats = []

    # loops through links
    for l in build_links(stat):
        site = requests.get(l, headers=headers) # get site info using requests

        # create BS object, sort through necessary info
        soup = BeautifulSoup(site.content, 'html.parser')
        ts = soup.find_all('td')

        # loop through BS object and add teams and stats to list
        for i in ts:
            team_stats.append(i.get_text())

    return team_stats
