__author__ = '29146'


# def findallPrime(n):
#
#     while n>0:
#         for i in range(2,n):
#             if n%i == 0:
#                 #x = False
#                 print str(n) + "not prime"
#
#             else:
#                 #x = True
#                 print str(n) + " prime"
#                 break
#
#         n-=1


for num in range(1,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print num


for i in range(2,97):
    if (97%i==0):
        print i
        print "not prime"
