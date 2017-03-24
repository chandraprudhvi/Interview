
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

c = arr

lenofarr = len(arr)

list1 = []
windowmax = []

for i in range(lenofarr):
    while window > 0:
        print window
        list1.append(arr[window])
        window -= 1
    print list1
    list1.sort()
    windowmax.append(list1[window -1])

    lenofarr-= 1
    arr.pop(0)

print windowmax






