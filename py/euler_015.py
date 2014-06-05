#!/usr/bin/python

"""
Problem 15
------------------------------------------------------------------------------
Starting in the top left corner of a 2x2 grid,
and only being able to move to the right and down,
there are exactly 6 routes to the bottom right corner.

__ __      __ 		  __
	 |		 |__       	|		|__ __         |__     		|
	 |			|		|__ 		  |			  |__   	|__ __


How many such routes are there through a 20x20 grid?
------------------------------------------------------------------------------
"""

import math

"""
	Will rapresent the moves as R=right, D=Down....
	In any grid of size N, we need N moves of each (R,D) (total 2N moves)
		ex for the 2x2 grid we have RRDD,RDRD,RDDR,DRRD,DRDR,DDRR (4 moves)
	If we arbitrary choose N of one direction first and fill the rest
	with other direction,
	the problem becomes a combination problem for N choices out of 2N
	so we could use the C(n,k) = n!/(k!(n-k)!) for the answer
	where n = 2N and k=N
"""


def euler_015(GRID_SIZE=20):
	n = 2 * GRID_SIZE
	k = GRID_SIZE
	return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))


if __name__ == '__main__':
    print(euler_015())
