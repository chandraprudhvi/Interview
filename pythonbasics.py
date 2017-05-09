__author__ = '29146'
import re

from collections import defaultdict

a = [1,2,3,4,5]
b = {'a':1,'b':2,'c':3,'d':4,'f':5,'e':6,'g':8}
b['prudhvi']= 10




print b.keys()
print b.values()
for i,j in b.iteritems():
    print i,j
c = (1,2,3,4,5,5)

d= {1,2,3,4,5,6,6}

print type(a)
print type(b)
print type(c)
print type(d)



x = 'prudhvi chandra'


m= list(x)
print sorted(m)

k = ''.join([a*2 for a in x])

print k

a = set(k)
b= list(a)

c = "a jkdnkjasdnbkja 11111 & ncjdksncjkas a 232323 &"

print re.findall('\d{1,6}\s\&',c)


a = defaultdict(lambda : 'a')

a['c']
a['b']
a['d']= "pudhvi"

print a.items()