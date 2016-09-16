from scipy import stats

def z_score(t_lst, s_lst):
    score = []
    stat = []
    team = []

    team = t_lst
    stat = s_lst

    for s in stat:
        score.append(float(s))
              
    score = ['%.2f' % s for s in stats.zscore(score)] 

    tm_zscore = dict(zip(team, score))

    return tm_zscore
