class Node():
    def __init__(self,data):

        self.data = data
        self.next = None

    def add(self,data):

        self.data = data

    def getnext(self):
        return self.next
    def addneext(self,next):
        self.next = next

class Linkedlist():
    def __init__(self):
        self.head = None

    def add(self,x):
        a =Node(x)
        a.addneext(self.head)
        self.head = a
    def gethead(self):
        return self.head.data
    def getnext(self):
        return self.head.next.data
    def size(self):
        x = 0
        c = self.head
        while c!= None:
            x+=1
            c = c.next
        return x
    def isempty(self):
        return self.head==None

    def delanode(self,x):

        c = self.head
        if c.data == x:
            c.next = None

        a = self.head.next


        while a != None:
            if a.data == x:
                t = a
                c.next = a.next
            c = c.next
            a = a.next






x = Linkedlist()
x.add(9)
x.add(10)
x.add(11)

print x.gethead()

print x.getnext()

print x.size()

print x.isempty()

x.delanode(10)

print x.getnext()
