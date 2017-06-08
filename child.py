__author__ = '29146'

class A:
    z = 3
    def test(self,x,y,z=None,o=None):
        if z==None:
            return x+y
        else:
            return x * y * z

    def args(self,*args, **idiot):

      print args[1]
      print idiot
      print idiot.keys()
      print idiot.values()




class B(A):
    x = A()


    #x.args(1,"xyz",3,4,5,6,7,7,8,8,8,8,8,8,8,firstname="a",b="a",)

    #print 5+x.z

class C(B):

    multiple = [1,2,3,4,5,6,7]
    m = B

    #print m.z

class D(B,C):

    f= B()
    k = C()

    print f.z + k.multiple[6]

    g = lambda i: i*2

    print g(1)

    list1 = [1,2,3,4,5,6,7]
    list2 = [9,7,6,5,4,3,2]

def x():

    for i in range(10):
        yield i

test = x()

print test.next()
print test.next()
print test.next()
print test.next()
    # a= map(lambda x: x * 2, [1,2,3,4])
    # print a


class base(object):
    def test(self):
        pass


class low1(object):
    def test(self):
        # super(low1, self).test()
        print "low1 test"


class low2(object):
    def test(self):
        # super(low2, self).test()
        print "low2 test"


class high(low1, low2, base):
    pass


if __name__ == "__main__":
    high().test()