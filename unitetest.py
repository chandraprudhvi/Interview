import unittest

def fun(x):
    return x + 1

def a(c):
    return c-1

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(fun(3), 4)
    def test_a(self):
        self.assertEqual(a(3), 2)
    def test_test(self):
        self.assertEqual(1,1)