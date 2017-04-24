__author__ = '29146'

import re
def fibonacci(x):

    a = 0
    b = 1

    yield a
    yield b

    for i in range(x):
        a,b = b , a+b
        yield b


# for i in fibonacci(10):
#     print i

def stringreverse(m):
    a = list(m)
    x= 0
    y = len(a)-1

    while x<y:
        temp = a[x]
        a[x]=a[y]
        a[y]=temp
        x+=1
        y-=1
    print ''.join(a)


stringreverse("prudhvi")



sdi = "this is prudhvi from India. who are you? prudhvi prudhvi 12345678"


print re.findall('prudhvi',sdi)
print re.search('from',sdi).group(0)


name = 'pruuuudhvi'
count = 0
for a in name:
    c = len(re.findall(a,name))
    count+=c

print count



if count > len(name):
    print "not unique"
else:
    print "unique"


