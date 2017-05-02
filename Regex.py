__author__ = '29146'

import re,urllib,sys

a = "This is Prudhvi Chandra. " \
    "Prudhvi is the the dany a don"

print re.split(r'(Prudhvi*)',a)
print re.findall('prudhvi',a,re.I)

print re.split('[0-9]',"10.60.70.229")


print re.findall('\d{1,5}\s\w+\s\w+\s\w*\s*\w+\s\d{1,5}',"nkldjnfklgjdfklgjndfkbvndfg1102 S abel street milpitas 95035grrgdergdrfgdfgdfgd101 E San Fernando Sanjose 95112fgdfbgdf")

try:
    u = urllib.urlopen("https://www.amazon.com/")
    text = u.read()

    print re.findall('<title>*.*</title>',str(text),re.I)[0]
except:
    e = sys.exc_info()[0]
    print e






print re.findall('\w+\s[1,8]',"abcdefghijabbaab 2418 fhjksfhjks klfjdsklfj 35635635 fhdjklsfhjkla")


##fibonacci

def fib(n):

    if type(n)==int:


            a,b = 0,1
            yield a
            yield b

            for i in range(n):
                a,b = b,a+b
                yield b
    else:
        print n + " is not an int"


for i in fib('a'):
    print i



    # String compression


def compressstring(a):

    res = ''
    count = 1
    res+=a[0]

    for i in range(len(a)-1):
        if a[i]==a[i+1]:
            count+=1
        else:
            if count>1:
                res+=str(count)
            res+=a[i+1]
            count=1
    if count>=1:
        res+=str(count)
    print res


compressstring("aaaabbnnnnnaac")




# String has unique charecters without datastructure


a = "pprudhvi"



if len(a) == len(set(a)):
    print "unique"
else:
    print "not unique"


# String has unique or not with DS

a = "pprudhvi"
x= {}

m = len(a)

for i in range(len(a)-1):
    if a[i] in x:
        x[a[i]]+=1
    else:

        x[a[i]]=1

for c,v in x.iteritems():

    if v>1:
        print "not unique"

#check permutation

a = "prudhvi"
b = "rudivhp"


if len(a)!=len(b):
    print "not possible"

c = list(a)

result = False
for i in b:
    if i in c:
        result = True
    else:
        result = False

if result == True:
    print "possible"
else:
    print "not possible"


#add some format in spaces in the string

a = "Mr John Smith"

b = a.replace(" ",'%20')
print b


#string rotation

a = 'prudhvi'
b = "ivhdurpis"

if a in b:
    print "true"







