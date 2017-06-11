__author__ = '29146'

def reverse():
    newname = input()

    su = list(newname)
    x=0
    y=len(su)-1
    while x<=y:
        temp = su[x]
        su[x] = su[y]
        su[y] = temp
        x+=1
        y-=1
    print ''.join(su)


reverse()






