#!/usr/bin/env python

"""
Author: Eltjon Metko
Problem 39 - Integer right triangles
-----------------------------------------------------------------------------
If p is the perimeter of a rightangle triangle with integral length sides, {a,b,c},
there are exactly three solutions for p = 120.
{20,48,52}, {24,45,51}, {30,40,50}
For which value of p <= 1000, is the number of solutions maximised?
-----------------------------------------------------------------------------
"""


def euler_039():
    s = {}
    # perimeter of right-agnle triangle is even and the smallest one is 12
    for p in xrange(12, 1001, 2):
        solutions = [(a, b, p - a - b)
                     for a in xrange(1, p / 3)
                     for b in xrange(a + 1, (p - a) / 2)
                     if a ** 2 + b ** 2 == (p - a - b) ** 2
                     ]
        if solutions:
            s[p] = solutions

    return sorted([(len(v), k) for k, v in s.iteritems()], reverse=True)[0][1]


if __name__ == '__main__':
    print(euler_039())
