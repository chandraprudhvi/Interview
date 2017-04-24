__author__ = '29146'

def fibonacci(x):

    a = 0
    b = 1

    yield a
    yield b

    for i in range(x):
        a,b = b , a+b
        yield b


for i in fibonacci(10):
    print i

