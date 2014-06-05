#!/usr/bin/python

"""
Problem 5
-----------------------------------------------------------------------------------------------------------
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
-----------------------------------------------------------------------------------------------------------
"""
import math

# since every number n in 1..10 has at least a 2*n in 11...20 it's enough
# to check if X is divisable by y in 11...20


def euler_005():
    max_num = math.factorial(20)

    # start at lcm(1...10) and increment at least with that
    for num in xrange(2520, max_num, 2520):
        rem = 0
        for x in xrange(11, 20):
            rem = num % x
            if rem:
                break

        if not rem:
            return num

    return max_num


if __name__ == '__main__':
    print(euler_005())
