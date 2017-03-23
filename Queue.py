__author__ = '29146'

def createQUEUE():
    queue = []
    return queue
    print queue

def enqueue(queue,items):
    queue.insert(0,items)
    print queue
def dequeue(queue):
    queue.pop()
    print queue

def size(queue):
    return len(queue)


queues = createQUEUE()

enqueue(queues,1)
enqueue(queues,10)
enqueue(queues,'dog')
dequeue(queues)
