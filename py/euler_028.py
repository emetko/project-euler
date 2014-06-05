#!/usr/bin/python

"""
Problem 28
---------------------------------------------------------------------------------------------------------
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:
			  73                      81
				 43	44 45 46 47 48 49 
					21 22 23 24 25 
					20  7  8  9 10 
					19  6  1  2 11 
					18  5  4  3 12 
					17 16 15 14 13 
				 37	36 35 34 33	32 31 
			  65 					  57

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
--------------------------------------------------------------------------------------------------------
"""
# layer 1: 					size 1
# layer 2: 3,5,7,9			size 3  diff_from_topright: -2
# layer 3: 13,17,21,25		size 5  diff_from_topright: -4
# layer 4: 31,37,43,49		size 7  diff_from_topright: -6
# layer 5: 57,65,73,81		size 9  diff_from_topright: -8
# notice that top-right value in any layer is size^2 and the other 3 corner values are obtained by repeatedly substracting size-1 from the top-right


def build_spiral(size):
	#start 2 diagonals with the common element
	diag_topright_downleft = []
	diag_topleft_downrigt = []

	counter = 0
	for i in xrange(3,size+1,2):
		max_value_for_size = i*i
		diag_topright_downleft.append(max_value_for_size)
		diag_topleft_downrigt.append(max_value_for_size-(i-1))
		diag_topright_downleft.append(max_value_for_size-2*(i-1))
		diag_topleft_downrigt.append(max_value_for_size-3*(i-1))
	return [diag_topleft_downrigt,diag_topright_downleft]

def euler_028(spiral_size=1001):
	spiral = build_spiral(spiral_size)
	return sum(spiral[0]) + sum(spiral[1]) + 1
	






if __name__ == '__main__':
    print(euler_028())

