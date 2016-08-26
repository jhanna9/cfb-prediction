def build_stat(file):
    d = {}
    with open(file) as f:
        for line in f:
            (key, val) = line.split()
            d[key] = val

    return d

def build_stat_position(file):
    d = {}
    with open(file) as f:
        for line in f:
            (key, val1, val2) = line.split()
            d[key] = val1, val2

    return d

print(build_stat('stat_num.txt'))

print(build_stat_position('stat_position.txt'))
