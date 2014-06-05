#!/usr/bin/python

"""
Problem 14
------------------------------------------------------------------------------
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence contains 10 terms.
Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
------------------------------------------------------------------------------
"""


def euler_014(NUM_LIMIT=1000000):
    max_length, answer = 1, 1
    for num in xrange(NUM_LIMIT):
        curr_length, curr_num = 1, num
        while num > 1:
            if num % 2:
                num = 3 * num + 1
            else:
                num = num / 2
            curr_length += 1
        if max_length < curr_length:
            max_length = curr_length
            answer = curr_num

    return answer


if __name__ == '__main__':
    print(euler_014())
