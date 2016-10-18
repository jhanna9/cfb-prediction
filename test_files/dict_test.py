def multi_team_dict(file):
    d = {}
    with open(file) as f:
        for line in f:
            (key, val1, val2) = line.split(',')
            d[key] = val1, val2.strip()
            
    return d

print(multi_team_dict('team_variation.txt'))
