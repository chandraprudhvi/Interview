__author__ = '29146'


def stringunique(a):
    for i in a:

        print i,a.find(i),a.rfind(i)

        if a.find(i) == a.rfind(i):
            c = "unique"

        else:
            c = "not unique"

    if c == "unique":
        print c
    else:
        print "not unique"

#stringunique("prudhvip")

def checkifpermutation(a,b):

    c = False

    if len(a) != len(b):
        c = False
        print "not permutation"
        return
    else:
        for i in a:
            if i in b:
                c = True
            else:
                c= False

    if c == True:
        print "Permutation"
    else:
        print "not permutation"


#checkifpermutation("dogg","ggod")


def fillspaceswith20(a):

    l = list(a)
    print l

    for i in range(len(l)):
        if l[i] == " ":
            l.pop(i)
            l.insert(i,"%20")

    print ''.join(l)
#fillspaceswith20("Mr John Smith ")


def findpermcanbeapali(a):

    length = len(a)
    odd = 0
    d = {}

    for i in a:
        if i in d:
            d[i]+=1
        else:
            d[i] = 1
    print d

    for i,j in d.iteritems():
        if j%2 != 0:
            odd+=1

    if length%2 ==0:
        if odd>0:
            print "not possible permutation"
    else:
        if odd == 1:
            print "possible"




#findpermcanbeapali("tactcoaaa")


def stringcompression(s):

    res = ""

    count = 1

    # Add in first character
    res += s[0]

    # Iterate through loop, skipping last one
    for i in range(len(s) - 1):
        if (s[i] == s[i + 1]):
            count += 1
        else:
            if (count > 1):
                # Ignore if no repeats
                res += str(count)
            res += s[i + 1]
            count = 1
    # print last one
    if (count >= 1):
        res += str(count)
    print res


#stringcompression("aaaabbggggccccdd")





