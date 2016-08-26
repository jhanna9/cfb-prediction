from soup import soup
from statistics import stdev

# loop to get yards per rushing attempt, get stand dev
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

    return round(stdev(yprush), 3)

print(yp_rush())
