#!/usr/bin/python
import sys
sys.path.insert(0, "..")

"""
Problem 7
------------------------------------------------------------------------------
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10 001st prime number?
------------------------------------------------------------------------------
"""
from utils.misc import is_prime, nth


def euler_007(INDEX=10001):
    # will exclude 2 and iterate only on the odd numbers and then get next to
    # last to compensate
    return nth((x for x in xrange(3, 9999999999, 2) if is_prime(x)), INDEX - 2)


if __name__ == '__main__':
    print(euler_007())
