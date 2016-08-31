# build stats dictionary from data file
def build_stat_dict(file):
    d = {}
    with open(file) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
            
    return d

# general link to stats
def build_links(stats):
    links = []

    link = "http://www.ncaa.com/stats/football/fbs/current/team/"

    stats_dict = build_stat_dict('stat_num.txt')       

    more_pgs = ['', '/p2', '/p3']

    for i in more_pgs:
        if stats in stats_dict:
            links.append(link + stats_dict[stats] + i)
        else:
            print("Stat not found")
            break
    print('links - ', stats)
    print(links)
    return links
