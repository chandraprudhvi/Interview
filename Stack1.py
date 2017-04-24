class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def bottom(self):
        return self.items[0]

    def size(self):
        return len(self.items)


x = Stack()
x.push(1)
x.push(2)
x.push(3)
print x.items
print x.peek()
print x.bottom()

x=[1,2,3,4,5]
x.insert(4,10)
print x

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def front(self):
        return self.items[len(self.items) - 1]

    def back(self):
        return self.items[0]

    def size(self):
        return len(self.items)


m = Queue()

m.enqueue(1)
m.enqueue(2)
m.enqueue(3)

print m.items

print m.front()
print m.back()


# implement queues with stack



