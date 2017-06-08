__author__ = '29146'

import sys

def string_reversal():
    a = raw_input()
    length =len(a)
    print length
    print a[::-1]

    x= ' jaffa '.join(reversed(a))
    #print x




string_reversal()