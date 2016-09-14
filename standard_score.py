from scipy import stats
from team_stat import team_stats

def z_score(two_lists):
    score = []
    stat = []
    team = []

    team, stat = two_lists

    for s in stat:
        score.append(float(s))
              
    score = ['%.2f' % s for s in stats.zscore(score)] 

    tm_zscore = dict(zip(team, score))

    return tm_zscore

print(z_score(team_stats()))
