__author__ = '29146'

def f(x,l=[]):
    print range(x)
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)


