#!/usr/bin/env python
import sys
sys.path.insert(0, "..")

"""
Author: Eltjon Metko
Problem 37 - Truncatable primes
-----------------------------------------------------------------------------
The number 3797 has an interesting property. Being prime itself,
it is possible to continuously remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.
Find the sum of the only eleven primes
that are both truncatable from left to right and right to left.
NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
-----------------------------------------------------------------------------
"""
from utils.sieves import primes


def truncate(strnum):
    t = set()
    for i in range(1, len(strnum)):
        t.add(int(strnum[i:]))
        t.add(int(strnum[:i]))
    return t


def euler_037():
    t = set()
    cache = set()
    for p in primes():
        pstr = str(p)
        if any(x in {2, 4, 5, 6, 8, 0} for x in pstr):
            continue
        if pstr[0] in [1, 9] or pstr[-1] in [1, 9]:
            continue
        cache.add(p)
        if len(pstr) > 1 and truncate(pstr).issubset(cache):
            t.add(p)
        # the problem states that there are only 11 such primes so break here.
        if len(t) == 11:
            break

    return sum(t)

if __name__ == '__main__':
    print(euler_037())

