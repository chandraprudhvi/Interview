__author__ = '29146'


def insertspace(a):
    m = list(a)
    x = 3

    while x<len(m):
        m.insert(x," ")
        x+=4



    print ''.join(m)





insertspace("prudhviprudhvi")

a="prudhvi:prudhvi"
print a.split(':')


a = [1,2,3,4,5,6,7,8,9,0]
b = [2,3,4]
print "reverse"
a = a.reverse()

print a
a.extend(b)

a.append(b)
print a



def findsubstring(a,b):
    if a in b:
        print "yes"
    else:
        print "no"

    print  b.count(a)
    print b.find(a)
    d=  b.center(len(a),'*')
    print b.endswith('t')
    print b.index("bad")
    print b.replace('prudhvi','shravan',1)
    print b.partition('is')
    print b.rstrip('iot')
    reversed(b)
    print b


findsubstring("prudhvi","prudhviurp is a bad boy prudhvipru is an idiot")