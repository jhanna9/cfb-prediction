import requests
from bs4 import BeautifulSoup
from links import build_links

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# list to hold all teams and selected stat
team_stats = []

# loop through the stat links to create a bs object
def soup(stat):
    for l in build_links(stat):
        site = requests.get(l, headers=headers) # get site info using requests
        # create BS object, sort through necessary info
        soup = BeautifulSoup(site.content)
        ts = soup.find_all('td')

        # loop through BS object and add teams and stats to list
        for i in ts:
            team_stats.append(i.get_text())

    return team_stats

print(soup('Scoring Defense'))
