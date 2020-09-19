# https://projecteuler.net/problem=9


from pythagorian_triples import Triple

for m in range(16, 23):

    if 500 % m != 0:
        continue

    n = int((500 / m) - m)

    t = Triple.from_euclid(m, n)

    print(t.equation())
    print("a+b+c =", t.a + t.b + t.c)
    print("abc =", t.a * t.b * t.c)
