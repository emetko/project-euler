#!/usr/bin/env python
import sys
sys.path.insert(0, "..")

"""
Author: Eltjon Metko
Problem 35 - Circular primes
-----------------------------------------------------------------------------
The number, 197, is called a circular prime
because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100:
2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
-----------------------------------------------------------------------------
"""
import itertools
from utils.sieves import primes
from collections import deque


def rotations(num):
    rot = set()
    d = deque(str(num))
    for i in range(len(str(num))):
        d.rotate(-1)
        rot.add(int(''.join(d)))
    return rot


def euler_035():
    circulars = []
    plist = set(itertools.takewhile(lambda x: x < 1000000, primes()))
    for p in plist:
        if p in circulars:  # this is found during previous rotations
            continue
        else:
            r = rotations(p)
            if r.issubset(plist):
                circulars.extend(r)

    return len(circulars)


if __name__ == '__main__':
    print(euler_035())
