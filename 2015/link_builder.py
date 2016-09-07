# a function to build links to specific statistics of ncaa football
import re

def build_link(filename, path):
    '''Combines link and stat code to create stat specific link

    Keyword arguments:
    filename -- file used to store stat codes
    
    returns: a dictionary


    '''
    # dictionaries used to create individual stat link
    stat_link = {}
    
    # matches stat code, creates, and stores link in dictionary with corresponding stat
    for line in filename:
        match = re.search(r'([\d]+).0">([\w\s]+)', line, re.IGNORECASE)
        if match:
            stat_link[match.group(2)] = path + match.group(1)
        else:
            print(False)

    return stat_link

