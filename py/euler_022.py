#!/usr/bin/python

"""
Author: Eltjon Metko
Problem 22
------------------------------------------------------------------------------
Using names.txt (right click and 'Save Link/Target As...'),
a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order.
Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to get a score.

For example,
when the list is sorted into alphabetical order,
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list.
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
------------------------------------------------------------------------------
"""
import string


def get_names(filename):
    names = []
    with open(filename) as f:
        for line in f:
            names = line.strip('"').split('","')
    names.sort()
    return names


def get_alpha_score(word):
    rdict = dict([(x[1], x[0]) for x in enumerate(string.ascii_lowercase, 1)])
    return sum(rdict[c.lower()] for c in word)


def euler_022(filename='../resources/names.txt'):
    return sum(index * get_alpha_score(name)
               for index, name in enumerate(get_names(filename), 1))


if __name__ == '__main__':
    print(euler_022())
