# https://projecteuler.net/problem=5

from math import floor


def is_palindrome(n: int) -> bool:
    n = str(n)

    mid_point = floor(len(n) / 2)

    left = n[:mid_point]
    right = ''

    if len(n) % 2 == 0:
        right = n[mid_point:]
    else:
        right = n[mid_point + 1:]

    return left == right[::-1]


from descending_product import PGenerator

for i in PGenerator(100, 999):
    if is_palindrome(i):
        print(i)
        break
