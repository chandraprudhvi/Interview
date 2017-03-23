__author__ = '29146'

# solution one
a = [1,2,3,4,5]

c = len(a) - 1
b = 0

while c > b:
   v= a[b]
   a[b] = a[c]
   a[c] = v
   c-=1
   b+=1
print a

# solution 2

a = [1,2,3,4,5]


