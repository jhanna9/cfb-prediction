# build stats dictionary from data file
def build_stat_dict(file):
    d = {}
    with open(file) as f:
        #if file == 'stat_num.txt':
        for line in f:
            (key, val) = line.split()
            d[key] = val
        '''else:
            for line in f:
                (key, val1, val2) = line.split()
                d[key] = val1, val2
        '''
            
    return d

# general link to stats
def build_links(stat):
    links = []

    link = "http://www.ncaa.com/stats/football/fbs/current/team/"
    
    stats_dict = build_stat_dict('stat_num.txt')

    #build_stat_dict('stat_position.txt')

    more_pgs = ['', '/p2', '/p3']

    for i in more_pgs:
        if stat in stats_dict:
            links.append(link + stats_dict[stat] + i)
        else:
            print("Stat not found")
            break

    return links 
