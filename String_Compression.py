__author__ = '29146'

from itertools import groupby
a= "aabbccdds"

l = [(len(tuple(g)),k) for k,g in groupby(a,str)]
print type(l)
print l

y= ' '.join(map(str, l))
print y