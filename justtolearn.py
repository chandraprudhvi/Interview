c =  dict = {'Name': ['Zara', 'meena' ,'sheela'], 'Age': 7, 'Class': 'First'}
#
# print c['Name'][1]
#
# print c['Age']
#
# m = c.values()
#
# print m
#
# print type(m)
# for i  in c.values():
#     print type(i)
#
#
#
# for k,v in c.iteritems():
#     if type(v) is list:
#         for i in range(len(v)):
#
#             print k, v[i]
#     else:
#         print k , v

# print c.items()
#
# print c.pop('Age')
#
# print c.items()
#
# c['Age'] = 7
#
# print c.items()
#
#
# d = c.copy()
#
# c.clear()
#
#
# print
#
# print d
#
# print c
#
# c['a'] =1
#
# print c
#
# c['a'] = 1
#
# print c
# c = d.copy()
#
# print c
#
# print c.viewitems()
# c['s'] = 12345567788888888
#
# print cmp(c,d)


# v = ()
# v = (1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,8,8,'add','jknvjksdnvjksdnvjkdsnvjkds')
# print cmp(v,v)
# print type(v)
#
# print max(v)
# x = {}
# print type(x)
#
# n = []
#
# # print type(n)
# b = [3,4,5]
# l =[]
# l.append('x')
# l.append(1)
# print l
# print l.count(1)
# print l.extend(b)
# print l
#
#
# l.insert(18 , 'a')
#
# l.reverse()
# l.sort()
#
# print l

#
# def isUniqueChars(string):
#
#   checker = 0
#   for c in string:
#     val = ord(c) - ord('a')
#     #print val
#     if (checker & (1 << val) > 0):
#
#       print "False"
#     else:
#       print checker
#       checker |= (1 << val)
#   print "True"
#
# isUniqueChars("prudhvi")


# def ifpalindromeperm():
#
#     stri = "aabcc"
#
#     c = len(stri)
#
#     a = {}
#     count = 0
#     for i in stri:
#         if i in a:
#
#             a[i]+=1
#         else:
#             a[i] = 1
#     print a
#     oddcount = 0
#     if (c%2 ==0):
#         for i in a.values():
#             if(i%2 !=0):
#                 print i
#                 oddcount+=1
#         if oddcount >0:
#             print "notpalindrome"
#         else:
#             print "palindrome"
#     oddcount =0
#     if (c%2 !=0):
#         for i in a.values():
#             #print i
#             if(i%2 >1):
#                 print i ,oddcount
#                 oddcount+=1
#         print oddcount
#         if oddcount >1:
#             print "notpalindrome"
#         else:
#             print "palindrome"
#
#     oddcount = 0
#
#
# ifpalindromeperm()


#%20

def sr():
    s = "Mr John Smith "
    l = []

    for m in s:
        if m ==' ':
            l.append('%20')
        else:
            l.append(m)
    print ''.join(l)
sr()


























