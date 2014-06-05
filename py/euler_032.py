#!/usr/bin/python

"""
Problem 32 - Pandigital Products
-----------------------------------------------------------------------------------
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
-----------------------------------------------------------------------------------
"""

import itertools
import string 
def pandigitals(num_digits):
	""" a permutation of digits 1 to max is guaranteed to be pandigital """ 
	return (''.join(x) for x in itertools.permutations(string.digits[1:num_digits+1]))

def identity_partitions(numstr):
	""" find 3 partions a,b,c of numstr for which a*b=c """
	return ((int(numstr[:i]),int(numstr[i:j]),int(numstr[j:]))
				for i in range(1,len(numstr)/2+1) 
				for j in range(i+1,len(numstr)/2+2) 
				if int(numstr[:i])*int(numstr[i:j])==int(numstr[j:]))

def euler_032(num_digits=9):
	return sum(set(prod for p in pandigitals(num_digits) for m1,m2,prod in identity_partitions(p)))
						 




if __name__ == '__main__':
    print(euler_032())

