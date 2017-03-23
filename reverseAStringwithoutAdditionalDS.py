
string = "shravan"


# a = len(string) - 1
# reverse=string[a]
#
# while a != 0:
#
#     a-=1
#
#     reverse+=string[a]
#
# print reverse
string = "prudhvi"
a = list(string)
#print a
x = 0
y = len(a)-1

while x<y:
#    #print a[x],a[y]
    c=a[x]
    a[x] = a[y]
    a[y] = c
    y -=1
    x +=1
#print a

print ''.join(a)


