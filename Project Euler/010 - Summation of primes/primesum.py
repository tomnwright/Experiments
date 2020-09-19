# https://projecteuler.net/problem=10

from math import sqrt


def is_factor(n, factor):
    return n % factor == 0


def is_prime(n: int, primes: list):
    limit = sqrt(n)
    for p in primes:
        if p > limit:
            break

        if is_factor(n, p):
            return False

    return True


def sum_primes(limit):
    """
    Calculate the sum of all prime numbers below
    a given limit.
    """

    primes = []

    total = 2  # already know 2

    if limit is not None:

        for i in range(3, limit, 2):

            if is_prime(i, primes):
                primes.append(i)

                total += i

    return total


print(sum_primes(2000000))
