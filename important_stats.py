from links import build_stat_dict
from soup import soup
from statistics import stdev, mean

# 
def impt_stat():
    for k, v in build_stat_dict('stat_position.txt').items():
        stat = soup(k)
        x = int(v)
        for s in stat:
            if x > len(stat):
                break
            else:
                if stat[x] == 'Passes_Intercepted' or stat[x] == 'Passes_Had_Intercepted':
                    stat.append(float(stat[x]))
                    x += (x + 3)
                else:
                    stat.append(float(stat[x]))
                    x += (x + 1)

    stat_mean = round(mean(yprush), 3)
    stat_sdev = round(stdev(yprush), 3)

    return stat_mean, stat_sdev

avg, sdev = impt_stat()
print(avg, sdev)


'''All stats are +1 from position to get the next relevant stat
except Pass Intercepted and Passes Had Intercpeted = +3 to next relevant stat
'''
