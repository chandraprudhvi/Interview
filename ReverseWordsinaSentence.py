sentence="The quick brown fox jumped over the lazy dog"

l = sentence.split()
print l

x = len(l) -1
y = 0

while x>y:
    c=l[y]
    l[y] = l[x]
    l[x] = c
    x-=1
    y+=1

m= ' '.join(l)
print m


#solution 2

l = m.split()
a =[]
c = len(l)-1
a.append(l[c])

while c >0:
    a.append(l[c-1])
    c-=1
print ' '.join(a)

