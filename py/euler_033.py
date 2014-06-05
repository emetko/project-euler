#!/usr/bin/python

"""
Author: Eltjon Metko
Problem 33 - Digit canceling fractions
-----------------------------------------------------------------------------
The fraction 49/98 is a curious fraction,
as an inexperienced mathematician in attempting to simplify it,
may incorrectly believe that 49/98 = 4/8,which is correct,
is obtained by cancelling the 9s.
We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction,
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms,
find the value of the denominator.
-----------------------------------------------------------------------------
"""
from fractions import gcd


def is_fake_fraction(a, b):
    if not b % 10:
        return False
    sa, sb = str(a), str(b)
    for d in sa:
        if d in sb:
            return float(a) / b == float(sa.replace(d, '', 1)) / float(sb.replace(d, '', 1))
    return False


def euler_033():
    denominator, numerator = 1, 1
    for a, b in [(n, d) for n in range(11, 100) for d in range(n + 1, 100) if is_fake_fraction(n, d)]:
        numerator *= a
        denominator *= b
    return denominator / gcd(numerator, denominator)


if __name__ == '__main__':
    print(euler_033())
