__author__ = '29146'

l = [1,2,3,4,5,6,7]

x = 5
d = {}
for i in range(len(l)):
    if (5-l[i]) in l:
        d[(l.index(l[i]))] = l.index((5-l[i]))
print d

for x,y in d.items():
    if y in d.values():
        d.pop(y)


print d


