from links import build_stat_dict
from soup import soupy
from statistics import stdev, mean

# 
def impt_stat():
    stat_mean_sdev = {}

    for k, v in build_stat_dict('stat_position.txt').items():
        ind_stat = []
        statistic = soupy(k)
        x = int(v)
        y = x + 1
        z = x + 3
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

        stat_mean = round(mean(ind_stat), 3)
        stat_sdev = round(stdev(ind_stat), 3)
    
        stat_mean_sdev[k] = (stat_mean, stat_sdev)

    return stat_mean_sdev
    
print(impt_stat())


'''Create dictionary of {name of stat: [mean, stdev]}
'''
