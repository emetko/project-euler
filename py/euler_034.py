#!/usr/bin/python

"""
Author: Eltjon Metko
Problem 34 - Digit factorials
-----------------------------------------------------------------------------
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers
which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
-----------------------------------------------------------------------------
"""

# If n is a natural number of d digits that is a factorion, then 10d - 1 <=1 n <= 9!d.
# This fails to hold for d >= 8 thus n has at most 7 digits, and the first upper bound is 9,999,999.
# But the maximum sum of factorials of digits for a 7 digit number is 9!7 = 2,540,160.
# Going further, 9!6 is 2,177,280, and the only 7 digit number not larger than 2,540,160 containing six 9's
# is 1,999,999, which is not a factorion by inspection.
# The next highest sum would be given by 1,999,998, yielding a third upper
# bound of 1,854,721.

import math


def euler_034():
    facts = [math.factorial(num) for num in range(10)]
    return sum(num for num in xrange(10, 1854721) if sum(facts[int(x)] for x in str(num)) == num)


if __name__ == '__main__':
    print(euler_034())
