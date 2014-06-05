#!/usr/bin/python

"""
Problem 3
-----------------------------------------------------------------------------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""


def euler_003(num=600851475143):
    for i in xrange(2, num + 1):
        while num % i == 0:
            num = num / i
            if num == 1 or num == i:
                return i


if __name__ == '__main__':
    print(euler_003())
