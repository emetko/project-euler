def gen_eratosthenes():
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2   # first integer to test for primality
    while True:
        if q not in D:
            yield q        # not marked composite, must be prime
            D[q * q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]:  # move each witness to its next multiple
                D.setdefault(p + q, []).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1


def factors(n):
    for p in primes():
        if p > n ** 0.5:
            break
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count:
            yield (p, count)
    if n != 1:
        yield (n, 1)

primes = gen_eratosthenes
