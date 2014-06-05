#!/usr/bin/python

"""
Problem 31 - Coin sums
-----------------------------------------------------------------------------
In England the currency is made up of pound, P, and pence, p, 
and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, P1 (100p) and P2 (200p).
It is possible to make P2 in the following way:

1P1 + 150p + 220p + 15p + 12p + 31p
How many different ways can P2 be made using any number of coins?
-----------------------------------------------------------------------------
"""

def euler_031():
	combos = [0]*201
	combos[0] = 1
	for x in [1,2,5,10,20,50,100,200]:
	    for i in xrange(x, 201):
	        combos[i] += combos[i-x]
	return combos[200]




if __name__ == '__main__':
    print(euler_031())

