
# REVERESE AN ARRAY
from array import *

arr = array('i',[1,2,3,4,5,6])



x = len(arr)-1
#print x
y =0

while x > y:

    c = arr[x]

    arr[x] = arr[y]
    arr[y] = c
    x-=1
    y+=1

#print arr

# find max in a window

window = 2
x = window
c = arr



lenofarr = len(arr)

list1 = []
windowmax = []

for i in range(lenofarr - window):
    while window >=0:

        list1.append(arr[window])
        window -= 1

    list1.sort()
    windowmax.append(list1[window])


    lenofarr-= 1
    arr.pop(0)
    window = x

    list1 = []

for x in  windowmax:
    print x




