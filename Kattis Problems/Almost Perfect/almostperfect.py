from math import *


def factors(n):
    result = []
    for i in range(1, n):
        if n % i == 0:
            result.append(i)

    return result


import sys

for line in sys.stdin:
    n = int(line)

    s = sum(factors(n))

    d = abs(s - n)

    if d == 0:
        print(n, "perfect")
    elif d <= 2:
        print(n, "almost perfect")
    else:
        print(n, "not perfect")