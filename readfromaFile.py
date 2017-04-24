# def fizzbuzz(n):
#
#     if n % 3 == 0 and n % 5 == 0:
#         return 'FizzBuzz'
#     elif n % 3 == 0:
#         return 'Fizz'
#     elif n % 5 == 0:
#         return 'Buzz'
#     else:
#         return str(n)
#
# print fizzbuzz(9)

# string reversal

# a = "prudhvi"
#
# m = len(a)
# x = 0
# z= list(a)
#
# while x<m:
#     c = z[x]
#     z[x] = z[m-1]
#     z[m-1] = c
#     x+=1
#     m-=1
#
#
# print ''.join(z)
# def bubbleSort(alist):
#     for x in range(len(alist)-1,0,-1):
#         for a in range(x):
#             if alist[a] > alist[a+1]:
#                 temp = alist[a]
#                 alist[a] = alist[a+1]
#                 alist[a+1] = temp
#
# alist = [54,26,93,17,77,31,44,55,20]
# bubbleSort(alist)
# print(alist)


# string reverselistoflists

# l = [[1,2,3,4],[6,7,8,9],[1,4,5,6,7,8]]
#
# def reverselalist(List):
#     x = List
#
#
#     m = len(x)
#     v = 0
#
#     while v <m:
#
#         temp = x[v]
#         x[v] = x[m-1]
#         x[m-1] = temp
#         m-=1
#         v+=1
#
#
#
#     return x
# reverselalist([[1,2,3,4],[6,7,8,9],[1,4,5,6,7,8]])
#
# def reverselistitems(x):
#     for c in range(len(x)):
#         print x[c]
#         reverselalist(x[c])
#     print x
#
#
# # def re(y):
# #     x = reverselalist(y)
# #     for c in range(len(x)-1):
# #
# #         reverselistitems(x[c])
# #     print x
# reverselistitems([[1,2,3,4],[6,7,8,9],[1,4,5,6,7,8]])



# a = "aaabbcccaammmmmm"

# d = []
# lastchar = ""
# count = 0
#
# for c in a:
#     if c == lastchar:
#         count+=1
#     else:
#         if lastchar != "":
#             d.append(lastchar+str(count))
#         count = 1
#     lastchar = c
# d.append(lastchar + str(count))
# print ''.join(d)


#
# d = []
# lastchar = ""
# count = 0
#
# for c in a:
#     if c == lastchar:
#         count+=1
#     else:
#         if lastchar!="":
#             d.append(lastchar+str(count))
#             count = 1
#         lastchar = c
#
# d.append(lastchar+str(count))
#
# print d


import itertools

# arr = [[1,2,3,4],
#        [12,13,14,5],
#        [11,16,15,6],
#        [10,9,8,7]]
#
# def print_spiral(arr):
#     while arr:
#         yield arr[0]
#
#         arr = list(reversed(zip(*arr[1:])))
#
#
# print list(itertools.chain(*print_spiral(arr)))
#
# print_spiral(arr)


a = ['a','b','c','d']

print list(itertools.combinations('abcdo',4))


shape_list = ["square", "triangle", "circle", "pentagon", "star", "octagon"]
g = list(itertools.cycle(shape_list))

print g

