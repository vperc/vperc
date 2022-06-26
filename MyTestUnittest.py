#! /usr/bin/python3

import unittest

class MyTestUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("This is setUpClass method")

    def testAOne(self):
        print("This is test01")

    def testCThree(self):
        print("This is testCThree")

    def testBTwo(self):
        print("This is testBTwo")

    def FourTest(self):
        print("This is FourTest")

    @classmethod
    def tearDownClass(cls):
        print("This is tearDownClass method")

if __name__ == '__main__':
    unittest.main(verbosity=2)
