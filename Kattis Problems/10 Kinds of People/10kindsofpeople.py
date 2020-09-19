class Vector2:
    def __init__(self, row: int = 0, column: int = 0):
        self.row = int(row)
        self.col = int(column)

    def __str__(self):
        return f"(Row {self.row}, Col {self.col})"

    def __add__(self, other: "Vector2"):
        t = type(other)
        if t is not Vector2:
            raise TypeError(f"unsupported operand type(s) for +: Vector2 and {t}")

        r = self.row + other.row
        c = self.col + other.col

        return Vector2(r, c)

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __mul__(self, other: int):
        t = type(other)
        if t is not int:
            raise TypeError(f"unsupported operand type(s) for *: Vector2 and {t}")

        r = self.row * other
        c = self.col * other

        return Vector2(r, c)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __eq__(self, other: "Vector2"):
        if type(other) is not Vector2:
            return super().__eq__(other)

        r = self.row == other.row
        c = self.col == other.col
        return r and c


class Grid:
    def __init__(self, c_width, rows=[]):
        self.c_width = c_width

        self.rows = rows

    def __getitem__(self, item):
        if isinstance(item, tuple):
            row, col = item
            return self.rows[row - 1][col - 1]

        if isinstance(item, Vector2):
            return self.rows[item.row - 1][item.col - 1]

        return self.rows[item - 1]

    def __setitem__(self, key, value):
        if type(value) is not bool:
            raise ValueError("Grid element must be boolean.")

        if isinstance(key, tuple):
            row, col = key
            self.rows[row - 1][col - 1] = value
            return

        if isinstance(key, Vector2):
            self.rows[key.row - 1][key.col - 1] = value
            return

        self.rows[key - 1] = value
        return

    def __str__(self):
        spaced_rows = [" ".join(["1" if i else "0" for i in row]) for row in self.rows]
        return "\n".join(spaced_rows)

    @property
    def r_height(self):
        """
        :return: Height (r value) of grid
        """
        return len(self.rows)

    def add_row(self, row: str):
        """
        Create grid row from 01 string
        :param row: String containing only 0s and 1s, of correct length
        """
        if len(row) != self.c_width:
            raise ValueError(f"Row must be of length {self.c_width}.")

        new_line = [char == "1" for char in row]
        self.rows.append(new_line)

    def valid_coord(self, coord: Vector2):
        r = (coord.row > 0) and (coord.row <= self.r_height)
        c = (coord.col > 0) and (coord.col <= self.c_width)
        return r and c

    def is_path(self, start: Vector2, end: Vector2) -> bool:

        start_val: bool = self[start]
        end_val: bool = self[end]

        if start_val is not end_val:
            return False

        start_bounds = Bounds.bounded_area(self, start)

        return end in start_bounds


class Bounds:
    directions = [
        Vector2(-1, 0),  # North
        Vector2(1, 0),  # South
        Vector2(0, 1),  # East
        Vector2(0, -1),  # West
    ]

    @staticmethod
    def bounded_area(grid: Grid, start: Vector2):

        found = [start, ]
        family: bool = grid[start]

        Bounds.recurse(start, grid, found, family)

        return found

    @staticmethod
    def recurse(target: Vector2, grid: Grid, found: list, family: bool):

        # recurse neighbours
        for direction in Bounds.directions:
            coord = direction + target

            if not grid.valid_coord(coord):
                continue  # invalid coordinate

            if coord in found:
                continue

            if grid[coord] is family:
                found.append(coord)
                Bounds.recurse(coord, grid, found, family)

    @staticmethod
    def bounds_to_string(bounds, r_size, c_size):
        rows = [[False for c in range(c_size)] for r in range(r_size)]
        temp = Grid(c_size, rows=rows)

        for bound in bounds:
            temp[bound] = True

        return str(temp)


def ints_input():
    return [int(i) for i in input().split(" ")]


# work out whether different users can move between given points on the grid using NSEW motion
# "binary" users have to stay on 0 points
# "decimal" users have to stay on 1 points

# size_r, size_c = ints_input()
# grid = Grid(size_c)
# for i in range(size_r):
#     grid.add_row(str(input()))
#
# # n, number of queries
# n = int(input())
#
# for i in range(n):
#     r1, c1, r2, c2 = ints_input()
#
#     start = Vector2(r1, c1)
#     end = Vector2(r2, c2)
#
#     path = grid.is_path(start, end)
#
#     if path:
#         print("decimal" if (grid[start] is True) else "binary")
#     else:
#         print("neither")
