import math
import itertools
import operator

def is_prime(n):
    """Returns True if n is prime"""
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    if n < 9:
        return True

    r = int(n ** 0.5)
    i = 5
    while i <= r:
        if n % i == 0:
            return False
        if n % (i + 2) == 0:
            return False

        i += 6

    return True


def fib_gen():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a


def mul(l):
    return reduce(operator.mul, l)


def is_pandigital(s):
    """ every digit must be present once....
      if any digit is present more that one it means that another is missing """
    return all(str(x) in s for x in range(1, 10))


def get_identities(n):
    """ return a list of identity(x*y) tuples """
    return [(x, n / x) for x in xrange(1, int(math.sqrt(n)) + 1) if n % x == 0]


def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(itertools.islice(iterable, n))


def vslice(iterable, low, high):
    """ return a value-based slice of the iterator instead index-based """
    return itertools.takewhile(lambda x: x < high, itertools.dropwhile(lambda x: x < low, iterable))


def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(itertools.islice(iterable, n, None), default)


def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(map(pred, iterable))


def flatten(listOfLists):
    "Flatten one level of nesting"
    return itertools.chain.from_iterable(listOfLists)


def get_divisors(n, only_proper=False):
    divisors = []

    d = 1
    while d * d < n:
        if n % d == 0:
            divisors.append(d)
            if not only_proper or d != 1:
                divisors.append(n / d)
        d += 1
    if d * d == n:
        divisors.append(d)

    return divisors


def accumulate2(iterable, func=operator.add):
    'Return running totals'
    # accumulate([1,2,3,4,5]) --> 1 3 6 10 15
    # accumulate([1,2,3,4,5], operator.mul) --> 1 2 6 24 120
    it = iter(iterable)
    total = next(it)
    yield total
    for element in it:
        total = func(total, element)
        yield total


def num_digits(num):
    if num > 0:
        return int(math.log10(num)) + 1
    elif num == 0:
        return 1
    else:
        return int(math.log10(-num)) + 2
