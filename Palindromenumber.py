__author__ = '29146'


a = 123321
t = a
count =0
# while a >0:
#     a = a/10
#     count+=1
#
# print count


l =[]

while a >0:

    b = a%10

    l.append(str(b))
    a = a/10

print l

l.reverse()
print l
print int(''.join(l))
if t == int(''.join(l)):
    print "palindrome"
else:
    print 'not'


num = 123321;
rev = 0;
while (num > 0):

    dig = num % 10
    rev = rev * 10 + dig
    num = num / 10

print rev