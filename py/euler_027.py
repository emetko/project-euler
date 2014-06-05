#!/usr/bin/python
import sys; sys.path.insert(0, "..")

"""
Problem 27
---------------------------------------------------------------------------------------------------------
Euler discovered the remarkable quadratic formula:

n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41^2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n^2 - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. 
The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:   n^2 + an + b, where |a| < 1000 and |b| < 1000 where |n| is the modulus/absolute value of n  (e.g. |11| = 11 and |4| = 4)
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
--------------------------------------------------------------------------------------------------------
"""
from utils.misc import is_prime

def euler_027(max_num = 1000):
	
	max_values = [0,0,0] #max_nr_primes,a,b

	for a in xrange(-1*max_num,max_num):
		for b in xrange(-1*max_num,max_num):
			curr_primes = 0
			for n in xrange(1000):
				if is_prime(n**2 + a*n + b):
					curr_primes += 1
				else: 
					break
			if curr_primes > max_values[0]:
				max_values = [curr_primes,a,b]

	return max_values[1]*max_values[2]





if __name__ == '__main__':
    print(euler_027())

