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


for num in range(2,101):
    prime = True
    for i in range(2,num):
        if (num%i==0):
            prime = False
    if prime:
       print num

#
# for i in range(2,97):
#     if (97%i==0):
#         print i
#         print "not prime"


# def adddata(func):
#     #func.data = 4
#     #func.kill = 10
#     def c(*args,**kwargs):
#         return "perfect"
#     return c
#
# def multipl(func):
#     def mul(**kwargs,**args):
#         return "ni"
#     return mul
#
# @multipl
# def add(x,y):
#     return x+y
#
#
#
#
#
#
#
# print add(3,4)
# import re
# a ="prudhvibbbbbbbhihhihihihihihihihihihi"
# x = list(a)
#
# m = len(x)
#
# count = 2







# while count<len(x):
#
#
#
#     print count
#     x.insert(count," ")
#     count+=3
#     print x


# print ' '.join(re.findall('.......',a))
#
#
# class TestClass(object):
#
#     def __init__(self, val):
#         print 'this is init', val
#         self.val = val
#
#     def __new__(cls, *args, **kwargs):
#         print 'this is new'
#         print args, kwargs
#         super(object, cls).__new__(*args, **kwargs)


# t = TestClass(10000)


# class ExceptionHelpers(object):
#
#     def instance_method(self):
#         print '10'
#
#     @classmethod
#     def exc_format(cls, format_type):
#         def outer_fn(test_fn):
#             def func(*args, **kwargs):
#                 try:
#                     return test_fn(*args, **kwargs)
#                 except Exception, e:
#                     if format_type == 'JSON':
#                         return {'error': e.message}
#                     else:
#                         return e.message
#             return func
#         return outer_fn
#
#
# @ExceptionHelpers.exc_format('ASDF')
# def test_1():
#     raise Exception("This is a message")
#
# print test_1()
#
# @ExceptionHelpers.exc_format('ABCD')
# def test_2():
#     raise Exception("Second Test")
#
# print test_2()
#
#
# ExceptionHelpers().instance_method()
#

# Old style class
# class Class():
#
#     def x(self):
#         return 'x'

# New style class
# class ClassNew(object):
#     pass
#
#
# print Class().x()
#
#
# class Parent1(object):
#
#     def a(self):
#         print 'a'
#
#     def b(self):
#         print 'b'


# class Parent2(object):
#
#     def b(self):
#         print 'xb'
#
#     def c(self):
#         print 'c'
#
#
# class Child(Parent1, Parent2):
#
#     def b(self):
#         print 'child b'
#         super(Child, self).b()
#
#     def overloaded(self, val1):
#         if type(val1) is str:
#             # do string stuff
#             print val1
#         elif type(val1) is int:
#             print val1 + 100
#
#     def area(self, length, width=None):
#         pass
#
#
# c = Child()
# c2 = Child()
# print c != c2
# c.b()
#
#
# class Child2(Child, Parent2):
#     pass
#
#
# c = Child2()
# c.b()
# print Child2.__mro__

#
# def fibanocci():
#     i, j = 0, 1
#     while True:
#         yield i + j
#         tmp = j
#         j = i+j
#         i = tmp
#
#
# def numbers_til(n):
#     for i in xrange(n):
#         yield i
#
#
# # 0 1 1 2 3 5 8 13..
# generator = fibanocci()
# print generator.next()
# print generator.next()
# print generator.next()
# print generator.next()
# print generator.next()
# print generator.next()
#
#
# # [1, 3, 5], [2, 4, 6, 7] -> 1, 2, 3, 4, 5, 6, 7
# def merge_generator(arr1, arr2):
#     i = 0
#     j = 0
#     while i < len(arr1) and j < len(arr2):
#         yield
#
#

# import time
#
#
# def timing_function(some_function):
#
#     """
#     Outputs the time a function takes
#     to execute.
#     """
#
#     def wrapper():
#         t1 = time.time()
#         some_function()
#         t2 = time.time()
#         return "Time it took to run the function: " + str((t2 - t1)) + "\n"
#     return wrapper
#
#
# @timing_function
# def my_function():
#     num_list = []
#     for num in (range(0, 10000)):
#         num_list.append(num)
#     print("\nSum of all the numbers: " + str((sum(num_list))))
#
#
# @timing_function
# def testdeco():
#     print "this is test deco"
#
#
# print my_function()
# print testdeco()

def addmessage(func):
    def printmessage():
        #func()
        print "this is a list"
    return printmessage()

@addmessage
def hell():

    a = [1,2,3,4,5,6,7]

    for i in a:
        print i


hell()