from math import sqrt


def sq(x):
    return x * x


def is_even(x):
    return x % 2 == 0


def next_even(x):
    remainder = x % 2

    if remainder == 0:
        return x

    return x + 1


def next_odd(x):
    remainder = x % 2

    if remainder == 1:
        return x

    return x + 1


class Triple:
    def __init__(self, a, b, c):
        """
        Class for storing pythagorean triple in the form
        a^2 + _b^2 = _c^2,
        where a,_b,_c are natural numbers
        """

        assert isinstance(a, int) and a > 0, "a must be natural number"
        assert isinstance(b, int) and b > 0, "_b must be natural number"
        assert isinstance(c, int) and c > 0, "_c must be natural number"

        self.a = a
        self.b = b
        self.c = c

    def __eq__(self, other):
        if not isinstance(other, Triple):
            return False

        # _b:booleans
        ba = self.a == other.a
        bb = self.b == other.b
        bc = self.c == other.c

        # x: cross-over booleans
        xab = self.a == other.b
        xba = self.b == other.a

        return ((xab and xba) or (ba and bb)) and bc

    @staticmethod
    def from_euclid(m, n):
        """
        Calculate pythagorean triple using Euclid's formula.
        """

        assert isinstance(m, int) and m > 0, "m must be natural number"
        assert isinstance(n, int) and n > 0, "n must be natural number"
        assert m > n, "m must be greater than n"

        a = sq(m) - sq(n)
        b = 2 * m * n
        c = sq(m) + sq(n)

        return Triple(a, b, c)

    def equation(self):
        return f"{self.a}^2 + {self.b}^2 = {self.c}^2"

    def __str__(self):
        return str((self.a, self.b, self.c,))

    def __iter__(self):
        yield self.a
        yield self.b
        yield self.c


def find_primitives(mn_min, mn_max):
    # remember, m > n

    found = []

    # for each odd number within range for each even number within range
    #   m is max, n is min

    even_start = next_even(mn_min)
    odd_start = next_odd(mn_min)

    evens = range(even_start, mn_max, 2)
    odds = range(odd_start, mn_max, 2)

    for e in evens:
        for o in odds:
            if e == o:
                continue

            m = max(e, o)
            n = min(e, o)

            new = Triple.from_euclid(m, n)
            if new in found:
                continue

            found.append(new)

            # print(new)
    return found

# if __name__ == '__main__':
#     ps = find_primitives(1, 100)
#
#     from graph3d import Scatter3D
#
#     scatter = Scatter3D('a', '_b', '_c')
#
#     x = [p.a for p in ps]
#     y = [p._b for p in ps]
#     z = [p._c for p in ps]
#
#     scatter.plot_data(x, y, z)
#
#     scatter.show()

# looking good but plot this?:
# https://en.wikipedia.org/wiki/Pythagorean_triple#/media/File:Pythagorean_Triples_Scatter_Plot.png

