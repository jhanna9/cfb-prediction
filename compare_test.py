d = {
     'a': ('a', 'a1', 'a2'),
     'b': ('b', 'b1', 'b2'),
     'c': ('c', 'c1', 'c2'),
     'd': ('d', 'd1', 'd2'),
     'e': ('e', 'e1', 'e2'),
    }

listo = ['a2', 'c1', 'f', 'b', 'g', 'e2', 'j', 'd']

no_list = []
good_list = []
x = 0

for l in listo:
    ind = listo.index(l)
    x = 0
    if listo[ind - 1] in no_list:
        continue
    for k, v in d.items():     
        if l in v:
            good_list.append(k)
            x = 0
            break
        elif x == len(d) - 1:
            no_list.append(l)          
        else:
            x += 1

print(no_list)
print(good_list)

# no_list = [f, g, j]
# good_list = [a, c]
# not in a list b, e2, d
