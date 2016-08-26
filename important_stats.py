from soup import soup
from statistics import stdev, mean

# loop to get yards per rushing attempt, get median and stand dev
def yp_rush():
    rush_o = soup('Rushing Offense')

    yprush = []
    x = 5
    for s in rush_o:
        if x > len(rush_o):
            break
        else:
            yprush.append(float(rush_o[x]))
            x += 8

    ypr_mean = round(mean(yprush), 3)
    ypr_sd = round(stdev(yprush), 3)

    return ypr_mean, ypr_sd

avg, sdev = yp_rush()
print(avg, sdev)
