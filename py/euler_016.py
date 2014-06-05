#!/usr/bin/python

"""
Problem 16
------------------------------------------------------------------------------
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
------------------------------------------------------------------------------
"""


def euler_016(base=2, exp=1000):
    return sum(int(x) for x in str(base ** exp))


if __name__ == '__main__':
    print(euler_016())
