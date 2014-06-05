#!/usr/bin/python

"""
Problem 6
------------------------------------------------------------------------------------------------
The sum of the squares of the first ten natural numbers is:
1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is:
(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum is 3025 - 385 = 2640

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum.
"""


def euler_006(NUMS=100):
    sum_of_squares, sum = 0, 0
    for num in xrange(1, NUMS + 1):
        sum += num
        sum_of_squares += num ** 2

    return sum ** 2 - sum_of_squares


if __name__ == '__main__':
    print(euler_006())
