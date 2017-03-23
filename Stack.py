__author__ = '29146'

import sys

def createstack():
    stack = []
    return stack
def push(item,stack):
    stack.append(item)
    print stack

def pop(stack):
    stack.pop()
    print stack

def peek(stack):
    print stack[len(stack)-1]

if __name__ == '__main__':
    stack = createstack()
    push(str(20),stack)
    push(str(40),stack)
    push(str(30),stack)

    pop(stack)
    peek(stack)