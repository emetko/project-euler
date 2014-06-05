#!/usr/bin/env python

"""
Author: Eltjon Metko
Problem 36 - Double-base palindromes
-----------------------------------------------------------------------------
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million,
which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base,
 may not include leading zeros.)
-----------------------------------------------------------------------------
"""


def euler_036():
    return sum(x for x in xrange(1000000)
               if str(x) == str(x)[::-1] and bin(x)[2:] == bin(x)[:1:-1])


if __name__ == '__main__':
    print(euler_036())
