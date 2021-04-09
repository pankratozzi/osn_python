import sys


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = float(real)
        self.imaginary = float(imaginary)

    def __str__(self):
        return '%.2f + %.2fi' % (self.real, self.imaginary)

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.real + other.real, self.imaginary + other.imaginary)
        else:
            sys.stderr.write('Not Complex Type!')

    def __radd__(self, other):
        self.__add__(other)

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            res_real = self.real * other.real - self.imaginary * other.imaginary
            res_img = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(res_real, res_img)
        else:
            sys.stderr.write('Not Complex Type!')

    def __rmul__(self, other):
        self.__mul__(other)


if __name__ == '__main__':
    cmx_1 = ComplexNumber(4, 5)
    cmx_2 = ComplexNumber(1, 3)
    cmx_3 = cmx_2 + cmx_1
    print(cmx_3)
    cmx_4 = cmx_2 * cmx_1
    print(cmx_4)
