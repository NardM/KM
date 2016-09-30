from fractions import Fraction
from abc import *


class Fractions(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, numerator, denominator, sign=1, intPart=0):
        self.sign = sign  # знак дроби (+ или -)
        self.intPart = intPart  # целая часть дроби
        self.numerator = numerator  # числитель дроби
        self.denominator = denominator  # знаменатель дроби


class Fract(Fractions):
    def __init__(self, numerator, denominator, sign=1, intPart=0):
        super().__init__(numerator, denominator, sign, intPart)
        self.A = (intPart * denominator + numerator) * sign
        self.B = denominator

    def __repr__(self):
        return 'Fract({}, {})'.format(self.A, self.B)

    def __str__(self):
        return '({}, {})'.format(self.A, self.B)

    def __add__(self, other):
        return Fract(self.A * other.B + other.A * self.B, self.B * other.B)

    def __radd__(self, other):
        return Fract(other * self.B + self.A, self.B)

    def __sub__(self, other):
        return Fract(self.A * other.B - other.A * self.B, self.B * other.B)

    def __rsub__(self, other):
        return Fract(other * self.B - self.A, self.B)

    def __mul__(self, other):
        return Fract(self.A * other.A, self.B * other.B)

    def __rmul__(self, other):
        return Fract(self.A * other, self.B)

    def __truediv__(self, other):
        return Fract(self.A * other.B, self.B * other.A)

    def __rtruediv__(self, other):
        return Fract(self.A, self.B * other)

    def __lt__(self, other):
        return self.A / self.B < other.A / other.B

    def __gt__(self, other):
        return self.A / self.B > other.A / other.B

    def __le__(self, other):
        return self.A / self.B <= other.A / other.B

    def __eq__(self, other):
        return self.A / self.B == other.A / other.B

    def __ne__(self, other):
        return self.A / self.B != other.A / other.B

    def __ge__(self, other):
        return self.A / self.B >= other.A / other.B

    def __del__(self):
        print("Вызван метод __del__()")

    def GetMixedView(self):
        number = self.A / self.B
        share = number - int(number) * self.sign
        n = int(number) * self.sign
        return "Целая часть " + str(n) + "\r\nДробная часть " + str(share)

    def Cancellation(self):
        return self.A / self.B * self.sign

    def GetIntPart(self):
        return self.A // self.B

    def Double(self):
        return self.A / self.B





A = Fract(5, 2)
B = Fract(6, 4)
a = Fraction(5, 2)
b = Fraction(6, 4)
print(A > B)
print(a > b)
print(3 / A)
