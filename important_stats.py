from links import build_stat_dict
from soup import soupy
from statistics import stdev, mean

# 
def impt_stat():
    for k, v in build_stat_dict('stat_position.txt').items():
        print('imp_stat - ', k)
        print('start pos - ', v)
        ind_stat = []
        statistic = soupy(k)
        print(statistic)
        x = int(v)
        y = x + 1
        print('increment - ', y)
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

    return stat_mean, stat_sdev
    

avg, sdev = impt_stat()

print(avg, sdev)


'''Create dictionary of {name of stat: [mean, stdev]}
'''
