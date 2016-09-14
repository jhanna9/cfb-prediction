from scipy import stats
from team_stat import team_stats

def z_score(two_lists):
    score = []
    stat = []
    team = []

    team, stat = two_lists

    stat = stats.zscore(stat)

    #score = ['%.2f' % s for s in stats.zscore(score)]

    for s in stat:
        score.append(stats.zscore(s))       

    tm_zscore = dict(zip(team, score))

    return tm_zscore

print(z_score(team_stats()))
