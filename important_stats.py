from links import build_stat_dict
from soup import soupy
from statistics import stdev, mean


def impt_stat():
    '''Iterates through each statistic's BS Object to get the important
       information.

       returns a dictionary
    '''
    
    # dictionary to hold the stat, mean, and standard deviation
    stat_mean_sdev = {}

    # builds then iterates through each stat's BS obj
    for k, v in build_dict('stat_position.txt').items():
        # list to store all important numbers per stat
        ind_stat = []
        
        # creates a BS object per stat
        statistic = soupy(k)

        # position of each important number within BS object list
        x = int(v)
        
        # variables to find the next important number
        y = x + 1
        z = x + 3

        # iterates through BS object to append important num to list
        for s in statistic:
            if x > len(statistic):
                break
            else:
                if k == 'Passes_Intercepted':
                    ind_stat.append(float(statistic[x]))
                    x += z
                else:
                    ind_stat.append(float(statistic[x]))
                    x += y

        # determines mean and standard deviation of each statistic
        stat_mean = round(mean(ind_stat), 3)
        stat_sdev = round(stdev(ind_stat), 3)
    
        # adds stat: (mean, stdev) to the dictionary
        stat_mean_sdev[k] = (stat_mean, stat_sdev)

    return stat_mean_sdev
