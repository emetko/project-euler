#!/usr/bin/python

"""
Problem 4
-----------------------------------------------------------------------------------------------
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def euler_004():
    return max(x * y for x in xrange(100, 1000) for y in xrange(100, 1000) if str(x * y) == str(x * y)[::-1])


if __name__ == '__main__':
    print(euler_004())
