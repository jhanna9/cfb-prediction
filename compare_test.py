d = {'a': ('a', 'a1', 'a2'), 'b': ('b', 'b1', 'b2'), 'c': ('c', 'c1', 'c2')}

listo = ['a2', 'c1', 'd', 'b']

no_list = []
good_list = []
x = 0

for l in listo:
    ind = listo.index(l)
    x = 0
    if listo[ind - 1] in no_list:
        break
    for k, v in d.items():     
        if l in v:
            good_list.append(k)
            x = 0
            break
        elif x == 2:
            no_list.append(l)          
        else:
            x += 1

#for l in listo:
#ind = listo.index(l)
#print(listo[(ind - 1)])


print(no_list)
print(good_list)
