yprush = []

# FUNCTION loop to get yards per rushing attempt, get median and stand dev
x = 5
for s in team_stats:
    if x > len(team_stats):
        break
    else:
        yprush.append(team_stats[x])
        x += 8
