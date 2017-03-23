class Node :
	def __init__( self, data ):
		self.data = data
		self.next = None
		self.prev = None

class LinkedList :
        def __init__( self ):
            self.head = None

        def add( self, data ):
            node = Node( data )
            if self.head == None :
                self.head = node
            else :
                node.next = self.head
                node.next.prev = node
                self.head = node

        def printlist(self):
            temp = self.head
            while(temp):
                print temp.data,
                temp= temp.next


l = LinkedList()

l.add( 'a' )
l.add( 'b' )
l.add( 'c' )
l.add('d')
l.add('e')
l.add('f')



l.printlist()


# reverse a linked list
r = Node(l.head)


