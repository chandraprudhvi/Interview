__author__ = '29146'

class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None


    def printlist(self):
        temp = self.head
        while(temp):
            print temp.data
            temp= temp.next



if __name__ == '__main__':
    llist = linkedlist()
    llist.head = node(1)
    #node.next = node(2)
    second = node(2)
    third = node(3)
    fourth= node(4)
    fifth = node(5)


    llist.head.next = second
    second.next= third
    third.next = fourth
    fourth.next = fifth

    llist.printlist()








