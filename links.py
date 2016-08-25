# general link to stats
def build_links(stat):
    links = []

    link = "http://www.ncaa.com/stats/football/fbs/current/team/"

    stats_dict = {'rush_o': '23', 'rush_d': '24'}

    more_pgs = ['', '/p2', '/p3']

    for i in more_pgs:
        if stat in stats_dict:
            links.append(link + stats_dict[stat] + i)
        else:
            print("stat not found")

    return links     
