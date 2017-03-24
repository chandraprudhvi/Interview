__author__ = '29146'

from array import *

arr = array('i' , [1,2,3,4,15,16,17,8])
value = 9
y = len(arr)
et = []

for i in range(y):

    x = value - arr[i]
    et.append(arr[i])
    y-=1

    if x in et:

        print "exists"
