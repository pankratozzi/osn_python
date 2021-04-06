class Cell:

    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.cell = '*' * int(self.cell_size)

    def __add__(self, other):
        if isinstance(other, Cell):
            other = other.cell_size
            return Cell(self.cell_size + other)
        else:
            print('Operation is available only for %s ' % self.__class__.__name__)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Cell):
            other = other.cell_size
            if self.cell_size < other:
                print('The Cell to sub is too small')
                return self
            else:
                return Cell(self.cell_size - other)
        else:
            print('Operation is available only for %s ' % self.__class__.__name__)

    def __mul__(self, other):
        if isinstance(other, Cell):
            other = other.cell_size
            return Cell(self.cell_size * other)
        else:
            print('Operation is available only for %s ' % self.__class__.__name__)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Cell):
            other = other.cell_size
            return Cell(self.cell_size // other) if self.cell_size > other \
                else Cell(other // self.cell_size)
        else:
            print('Operation is available only for %s ' % self.__class__.__name__)

    def make_order(self, line_len):
        res = ''
        for x in range(0, len(self.cell), line_len):
            if len(self.cell[x:]) >= len(self.cell) // line_len:
                res += '%s\n' % self.cell[x:line_len+x]
            else:
                res += '%s' % self.cell[x:]
        return res

    def __str__(self):
        return 'Cell: <%s>' % self.cell


cell_1 = Cell(5)
cell_2 = Cell(4)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
cell_3 = Cell(25)
print('The string is: "%s"' % cell_3.make_order(7).replace('\n', ', '))
print(cell_3.make_order(7))
