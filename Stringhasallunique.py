__author__ = '29146'

import re

def ifstringunique(sample):
    k = 0
    for x in sample:
        #print x
        z = len(re.findall(x,sample))
        k+=z

    #print k
    if k > len(sample):
        return "false"
    else:
        return "true"




if ifstringunique('pruudhvi') == "false":
    print "not unique"
else:
    print "unique"