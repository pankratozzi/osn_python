from copy import deepcopy


class Matrix:
    def __init__(self, matrix):
        self.mtx = list(matrix)

    def __getitem__(self, item):
        return self.mtx[item]

    def __add__(self, other):
        if isinstance(other, Matrix):
            other = other.mtx
        result = deepcopy(self.mtx)
        try:
            for idx in range(len(result)):
                for jdx in range(len(result[0])):
                    result[idx][jdx] += other[idx][jdx]
        except TypeError:
            print('Cannot concatenate non list or non Matrix objects!')
        return Matrix(result)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            other = other.mtx
        result = deepcopy(self.mtx)
        try:
            for idx in range(len(result)):
                for jdx in range(len(result[0])):
                    result[idx][jdx] -= other[idx][jdx]
        except TypeError:
            print('Cannot sub non list or non Matrix objects!')
        return Matrix(result)

    def __mul__(self, other):
        result = deepcopy(self.mtx)
        if isinstance(other, Matrix):
            other = other.mtx
        elif isinstance(other, int) or isinstance(other, float):
            for idx in range(len(result)):
                for jdx in range(len(result[0])):
                    result[idx][jdx] *= other
            return Matrix(result)
        try:
            for idx in range(len(result)):
                for jdx in range(len(result[0])):
                    result[idx][jdx] *= other[idx][jdx]
        except TypeError:
            print('Cannot multiply non list or non Matrix objects!')
        return Matrix(result)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __str__(self):
        out_mtx = ''
        for el in self.mtx:
            out_mtx += (str(el).replace('[', '|').replace(']', '|') + "\n")
        return out_mtx

    @staticmethod
    def reshape_loc(result):
        for x in result:
            if not any(x):
                result.remove(x)
        return Matrix(result)


class MatrixVector(Matrix):

    def __mul__(self, other):
        """
        works only for 1st argument - Matrix, 2nd argument - vector
        length Matrix list <= length Vector list
        """
        if isinstance(other, MatrixVector):
            other = other.mtx
        result = deepcopy(self.mtx)
        if len(result) < len(other):
            while len(result) < len(other):
                result.extend([[0]])
        for idx in range(len(other)):
            while len(result[idx]) < len(other):
                result[idx].extend([0])
        for idx in range(len(result)):
            for jdx in range(len(result[idx])):
                result[idx][jdx] *= other[jdx][0]
        return Matrix(result)

    def __add__(self, other):
        # shorter and faster
        if isinstance(other, MatrixVector):
            other = other.mtx
        return MatrixVector([[col1 + col2 for col1, col2 in zip(row1, row2)] for
                             row1, row2 in zip(self.mtx, other)])


mat = [[1, 2, 0, 1], [3, 4, 5, 1], [0, 2, 3, 1]]
ls = [[1, 1, 0, 1], [1, 2, 1, 1], [1, 1, 0, 1]]
mtx = Matrix(mat)
mtx_2 = Matrix(ls)
print('ADD')
add_mat = mtx + mtx_2
print(add_mat, type(add_mat))
print('SUB')
print(mtx - mtx_2)
print('MULTIPLY')
print(mtx * mtx_2)
right_mul = 1.5 * mtx
print('MULTIPLY right DIGIT')
print(right_mul)
print('VECTOR')
mtx1 = [[2, 2, 2], [1, 1]]
vector = [[1], [2], [3]]
mtx1 = MatrixVector(mtx1)
mtx2 = MatrixVector(vector)
mat_vector = mtx1 * mtx2
print(mat_vector)
mat_vector = mat_vector.reshape_loc(mat_vector.mtx)
print('DEL ZERO SHAPE')
print(mat_vector)
print('ADD')
new_mtx1 = MatrixVector(mat)
new_mtx2 = MatrixVector(ls)
print(new_mtx1 + new_mtx2)
