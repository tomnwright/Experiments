# https://open.kattis.com/problems/cd

from sys import stdin


class InputData:
    def __init__(self):
        self.data = stdin.readlines()
        self.current = 0

    def next(self, n = None):
        if n is None:
            self.current += 1
            return self.data[self.current - 1]

        start = self.current
        self.current += n

        return self.data[start:self.current]


inp = InputData()

while True:
    jack_total, jill_total = map(int, str(inp.next()).split(" "))

    if jack_total + jill_total == 0:
        break

    jack_cds = map(int, inp.next(jack_total))
    jill_cds = map(int, inp.next(jill_total))

    common = len(set(jack_cds).intersection(jill_cds))
    print(common)
