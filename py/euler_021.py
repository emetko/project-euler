#!/usr/bin/python
import sys; sys.path.insert(0, "..")

"""
Problem 21
---------------------------------------------------------------------------------------------------------
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
----------------------------------------------------------------------------------------------------------
"""
from utils.misc import get_divisors

def euler_021(MAX_NUM = 10000):
	d = {}
	amicables = set()
	for num in xrange(3,MAX_NUM):
		if num not in amicables: #we have already found this
			if not d.has_key(num):
				d[num] = sum(get_divisors(num,True))
			candidate = d[num]
			if candidate != num:
				if not d.has_key(candidate):
					d[candidate] = sum(get_divisors(candidate,True))
				if d[num] == candidate and num == d[candidate]:
					amicables.add(num)
					amicables.add(candidate)
	
	return sum(amicables)





if __name__ == '__main__':
    print(euler_021())

