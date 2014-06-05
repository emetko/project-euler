#!/usr/bin/python
from collections import defaultdict
import sys


def color(s, status=''):
    if not sys.stdout.isatty():
        return s
    colors = {'OK': '\033[92m',
              'WARNING': '\033[93m',
              'KO': '\033[91m',
              '': ''}
    ENDC = '\033[0m'
    return colors[status] + s + ENDC


def OK(s):
    print(color(s + '...\t[OK]', 'OK'))


def KO(s, error):
    print(color(s + '...\t[FAIL]', 'KO') + ' | ' + error)

answers = defaultdict(str)


def load_answers():
    ANSWERS_STORE = '../answers'
    with open(ANSWERS_STORE) as f:
        for line in f:
            k, v = line.strip().split('|')
            answers[k] = v

    return answers


def test_euler(num):
    filename = "{0:03d}".format(num)

    mod = __import__('euler_' + filename, globals(), locals(), ['*'])

    f = getattr(mod, 'euler_' + filename)
    expected = answers[str(num)]
    result = str(f())

    try:
        assert result == expected
        OK(filename)
    except AssertionError:
        KO(filename, str(expected) + " != " + str(result))


load_answers()
for i in range(1, 30):
    test_euler(i)
