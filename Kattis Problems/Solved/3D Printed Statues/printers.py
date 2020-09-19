from math import pow, floor, ceil, log2
n = int(input())
p = floor(log2(n))
print(p + ceil(n / pow(2, p)))

import math