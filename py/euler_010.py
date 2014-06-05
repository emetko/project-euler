#!/usr/bin/python
import sys
sys.path.insert(0, "..")

"""
Problem 10
-----------------------------------------------------------------------------------------------------
The sum of primes below 10 is 2+3+5+7 = 17
Find the sum of all primes below two million
-----------------------------------------------------------------------------------------------------
"""
from utils.misc import vslice
from utils.sieves import primes


def euler_010(MAX_NUM=2000000):
    return sum(x for x in vslice(primes(), 1, MAX_NUM))


if __name__ == '__main__':
    print(euler_010())
