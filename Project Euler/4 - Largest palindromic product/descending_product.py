class PGenerator:
    def __init__(self, n_min, n_max):
        self.min = n_min
        self.max = n_max

        self.queue = [PChild(n_max, n_min, n_max), ]
        self.yielded = []

    def __iter__(self):
        while len(self.queue) > 0:
            # get next child
            next_child: PChild = max(self.queue, key=lambda child: child.prod_next)

            if not next_child.active:
                self.activate(next_child)

                if next_child.prod_next in self.yielded:
                    self.update_children()
                    continue

            yield_val = next_child.prod_next
            self.yielded.append(yield_val)
            yield yield_val

            self.update_children()

    def update_children(self):
        to_remove = []

        for e, child in enumerate(self.queue):
            if not child.active:
                continue

            child.update_next(self)

            if child.mul_next < self.min:
                to_remove.append(e)

        for i in to_remove:
            del self.queue[i]

    def add_child(self, n):
        new_child = PChild(n, self.min, self.max)
        self.queue.append(new_child)

    def activate(self, child: "PChild"):
        child.active = True

        new_n = child.n - 1
        if new_n >= self.min:
            self.add_child(new_n)


class PChild:
    def __init__(self, n, mul_min, mul_max):
        self.n = n
        self.mul_min = mul_min

        self.mul_next = mul_max
        self.prod_next = n * self.mul_next

        self.active = False

    def update_next(self, master: PGenerator):
        self.mul_next = self.get_next_multiplier(master)
        self.prod_next = self.mul_next * self.n

    def get_next_multiplier(self, master: PGenerator):
        m = self.mul_next
        while m >= self.mul_min:
            p = m * self.n

            if p not in master.yielded:
                return m

            m -= 1

        return m

if __name__ == '__main__':
    for i in PGenerator(1, 10):
        print(i)