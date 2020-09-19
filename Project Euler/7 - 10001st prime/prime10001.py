# https://projecteuler.net/problem=7
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


def nth_prime(n, limit=None):
    assert n > 0, "n (nth number) must be positive"

    primes = []

    total = 1  # already know 2
    if n == 1:
        return 2

    if limit is not None:

        for i in range(3, limit + 1, 2):

            if is_prime(i, primes):
                primes.append(i)

                total += 1

                if total >= n:
                    return i

        raise Exception(f"Limit exceeded: {n}th prime not found.")

    i = 1
    while True:
        i += 2

        if is_prime(i, primes):
            primes.append(i)

            total += 1

            if total >= n:
                return i


print(nth_prime(10001))

#  ### TIME TEST ###  #

import time
total = 0
for i in range(100):
    start = time.time()
    nth_prime(10001)
    total += time.time() - start

print(total / 100)