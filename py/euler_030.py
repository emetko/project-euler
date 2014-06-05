#!/usr/bin/python

"""
Problem 30
---------------------------------------------------------------------------------------------------------
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
--------------------------------------------------------------------------------------------------------
"""
def find_upper_limit(power):
	n = 9**power         #worse upper limit will be the sum of n powers of for the maximum digit (9)
	lower_guess = len(str(n))*n
	return len(str(lower_guess))*n #up the upper limit to at least the number lower_guess digits.

def euler_030(power = 5):
	return sum(num for num in xrange(2,find_upper_limit(power)) if sum(int(x)**power for x in str(num))==num)







if __name__ == '__main__':
    print(euler_030())

