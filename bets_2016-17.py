import requests
from bs4 import BeautifulSoup

# use to get around firewalls blocking scrapes
headers = {'User-agent': 'Mozilla/5.0'}

# links to stats sites
links = ["http://www.ncaa.com/stats/football/fbs/current/team/23",
        "http://www.ncaa.com/stats/football/fbs/current/team/23/p2",
        "http://www.ncaa.com/stats/football/fbs/current/team/23/p3"]

# list to hold all teams and stats
team_stats = []

# loop through the links
for l in links:
    site = requests.get(l, headers=headers) # get site info using requests
    # create BS object, sort through necessary info
    soup = BeautifulSoup(site.content)
    ts = soup.find_all('td')

    # loop through BS object and add teams and stats to list
    for i in ts:
        team_stats.append(i.get_text())
 
print(team_stats)

'''
need to sort through the list
extract teams and stats to combine them to a dictionary
need to handle '-' for ties in team rankings
'''
