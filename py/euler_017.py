#!/usr/bin/python

"""
Problem 17
------------------------------------------------------------------------------
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 inclusive were written out in words,
how many letters would be used?


NOTE: Do not count spaces or hyphens.
For example, 342 (three hundred and forty-two) contains 23 letters
		 and 115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
------------------------------------------------------------------------------
"""


def int2word(number):
    if number == 1000:
        return 'one thousand'

    num = ['', 'one', 'two', 'three', 'four',
           'five', 'six', 'seven', 'eight', 'nine']
    num.extend(['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen'])
    num.extend(tens if ones == '' else (tens + "-" + ones)
               for tens in ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
               for ones in num[0:10])

    hundrends = number / 100
    units = number % 100

    word = ''
    if hundrends:
        word = num[hundrends] + ' hundred'
        if units:
            word += ' and '
    word += num[units]
    return word


def euler_017(MAX_NUM=1000):
    return len([x for num in xrange(MAX_NUM + 1) for x in int2word(num) if x not in [' ', '-']])


if __name__ == '__main__':
    print(euler_017())
