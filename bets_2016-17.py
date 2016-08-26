import requests
from bs4 import BeautifulSoup
from links import build_links

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# DATA IN DIFFERENT FILElinks to stats sites
'''links = ["http://www.ncaa.com/stats/football/fbs/current/team/23",
        "http://www.ncaa.com/stats/football/fbs/current/team/23/p2",
        "http://www.ncaa.com/stats/football/fbs/current/team/23/p3"]
'''

# list to hold all teams and stats
team_stats = []
yprush = []

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

# FUNCTION loop to get yards per rushing attempt, get median and stand dev
x = 5
for s in team_stats:
    if x > len(team_stats):
        break
    else:
        yprush.append(team_stats[x])
        x += 8

print(soup('rush_o'))
print(yprush)
print(len(yprush))
        

'''
need to sort through the list to
extract teams / stats to combine them to a dictionary
need to handle '-' for ties in team rankings
'''
