d = {'a': ('a', 'a1', 'a2'), 'b': ('b', 'b1', 'b2'), 'c': ('c', 'c1', 'c2')}

listo = ['a2', 'c1', 'd', 'b', 'e']

no_list = []
good_list = []
x = 0

for l in listo:
    x = 0
    for k, v in d.items():     
        if l in v:
            good_list.append(k)
            x = 0
            break
        elif x == 2:
            no_list.append(l)          
        else:
            x += 1

print(no_list)
print(good_list)
