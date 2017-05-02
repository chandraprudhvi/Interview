__author__ = '29146'


def printdaimond(rows):

    # for i in range(rows):
    #     print (' '*(rows-i)+ '* '*(i))
    # for j in range(rows-1,0,-1):
    #     print (' '*(rows-j)+ '* '*(j))









    for i in range(rows):
        print ' '*(rows-i) + '* '*(i)
    for i in range(rows-1,0,-1):
        print ' '*(rows-i) + '* '*(i)



printdaimond(11)


def pyramid(rows):

    for i in range(rows):
        print ' '*(rows-i-1)+'* '*(i+1)

pyramid(10)

print '/' * 100
def reversepyramid(rows):

    for i in range(rows-1,0,-1):
        print (' '*(rows -i)+'* '*i)

reversepyramid(10)


def charectersinreverse(a):
    b = len(a)

    for i in range(b-1,0,-1):
        #print i
        print a[i]

charectersinreverse("prudhvi")




