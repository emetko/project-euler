#!/usr/bin/python
import sys; sys.path.insert(0, "..")

"""
Problem 23
---------------------------------------------------------------------------------------------------------
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers 
is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
----------------------------------------------------------------------------------------------------------
"""
from utils.misc import get_divisors

def get_abundant_numbers(max_num):
	return [x for x in xrange(12,max_num) if sum(get_divisors(x,only_proper=True))>x]


def get_possible_sums(max_num):
	abundant_numbers = get_abundant_numbers(max_num)
	return set(a+b for a in abundant_numbers for b in abundant_numbers if a+b<max_num)
	

def euler_023(MAX_NUM = 28124):
	sum_of_ab = get_possible_sums(MAX_NUM)
	return sum(x for x in xrange(MAX_NUM) if x not in sum_of_ab)





if __name__ == '__main__':
    print(euler_023())

