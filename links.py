# build stats dictionary from data file
def build_stat_dict(file):
    '''Builds a dictionary from a data file with key = statistic and value = either a
       number related to the website link or the stat position in a table.

        Keyword arguments:
        file -- name of data file

        return a dictionary
    '''

    # dictionary to return
    d = {}
    
    # opens file, reads line in file, splits line, stores split into dictionary
    with open(file) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val
            
    return d

def build_links(stats):
    '''Builds links to all team statistics.

       Keyword arguments:
       stats -- name of the statistic to build the links for

        returns a list
    '''

    # list to return
    links = []

    # the standard prefix for each statistic
    link = "http://www.ncaa.com/stats/football/fbs/current/team/"

    # builds the statistics dictionary with corresponding web path number
    stats_dict = build_stat_dict('stat_num.txt')       

    # the suffixes to obtain 3 pages of teams/stats
    more_pgs = ['', '/p2', '/p3']

    # builds links for each statistic if it is in the stats dictionary
    for i in more_pgs:
        if stats in stats_dict:
            links.append(link + stats_dict[stats] + i)
        else:
            print("Stat not found")
            break
    
    return links
