#!/usr/bin/python

"""
Problem 9
------------------------------------------------------------------------------
A Pythagorean triplet is a set of three natural numbers, a < b < c,
for which a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists only one Pythagorean triplet for which a + b + c = 1000
find the product a*b*c
------------------------------------------------------------------------------
"""
# loop optimisations:
# 0 < a < 333 because its natural and a=1000-b-c where c>b>a
# b max possible value is 499 to allow for 1+b+c=1000 where c>b
# c max possible value is 997 (in the case of a=1,b=2)


def euler_009(num=1000):
    res = [a * b * (num - a - b)
           for a in xrange(1, num / 3)
           for b in xrange(a + 1, (num - a) / 2)
           if a ** 2 + b ** 2 == (num - a - b) ** 2
           ]
    return res[0]


if __name__ == '__main__':
    print(euler_009())
