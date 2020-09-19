#https://projecteuler.net/problem=3

from math import sqrt

def largest_pf(n):
    """
    Calculates the largest prime factor p of a positive integer n.
    :param n: Positive integer > ?
    :return: Largest prime factor
    """

    # based on the assumption that the largest factor of n
    # will either be p or pk: the product of p and other prime factors.

    # p will also be the largest prime factor of pk.

    # largest possible factor = sqrt(n)
    stop = int(sqrt(n)) + 1

    for i in range(2, stop):

        if n % i == 0:

            factor = int(n / i)

            return largest_pf(factor)

    return n


print(largest_pf(600851475143))
