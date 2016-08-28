def build_stat_dict(file):
    d = {}
    with open(file) as f:
        if file == 'stat_num.txt':
            for line in f:
                (key, val) = line.split()
                d[key] = val
        else:
            for line in f:
                (key, val1, val2) = line.split()
                d[key] = val1, val2
            
    return d

print(build_stat_dict('stat_num.txt'))

print(build_stat_dict('stat_position.txt'))
