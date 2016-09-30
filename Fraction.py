from fractions import Fraction
from abc import *


class Fractions(metaclass=ABCMeta):
    __metaclass__ = ABCMeta

    def __init__(self, numerator, denominator, sign=1, intPart=0):
        self.__sign = sign  # знак дроби (+ или -)
        self.__intPart = intPart  # целая часть дроби
        self.__numerator = numerator  # числитель дроби
        self.__denominator = denominator  # знаменатель дроби


class Fract(Fractions):
    def __init__(self, numerator, denominator, sign=1, intPart=0):
        """
        :rtype: int, int, int, int
        """
        super().__init__(numerator, denominator, sign, intPart)
        self.__A = (intPart * denominator + numerator) * sign
        self.__B = denominator

    def __repr__(self):
        return 'Fract({}, {})'.format(self.__A, self.__B)

    def __str__(self):
        return '({}, {})'.format(self.__A, self.__B)

    def __add__(self, other):
        return Fract(self.__A * other.__B + other.__A * self.__B, self.__B * other.__B)

    def __radd__(self, other):
        return Fract(other * self.__B + self.__A, self.__B)

    def __sub__(self, other):
        return Fract(self.__A * other.__B - other.__A * self.__B, self.__B * other.__B)

    def __rsub__(self, other):
        return Fract(other * self.__B - self.__A, self.__B)

    def __mul__(self, other):
        return Fract(self.__A * other.__A, self.__B * other.__B)

    def __rmul__(self, other):
        return Fract(self.__A * other, self.__B)

    def __truediv__(self, other):
        return Fract(self.__A * other.__B, self.__B * other.__A)

    def __rtruediv__(self, other):
        return Fract(self.__A, self.__B * other)

    def __lt__(self, other):
        return self.__A / self.__B < other.__A / other.__B

    def __gt__(self, other):
        return self.__A / self.__B > other.__A / other.__B

    def __le__(self, other):
        return self.__A / self.__B <= other.__A / other.__B

    def __eq__(self, other):
        return self.__A / self.__B == other.__A / other.__B

    def __ne__(self, other):
        return self.__A / self.__B != other.__A / other.__B

    def __ge__(self, other):
        return self.__A / self.__B >= other.__A / other.__B

    def __del__(self):
        print("Вызван метод __del__()")

    def get_mixed_view(self):
        """преобразование дроби в смешанный вид"""
        number = self.__A / self.__B
        share = number - int(number) * self.__sign
        n = int(number) * self.__sign
        return "Целая часть " + str(n) + "\r\nДробная часть " + str(share)

    def cancellation(self):
        """сокращения дроби"""
        return self.__A / self.__B * self.__sign

    def get_int_part(self):
        """выделения целой части дроби"""
        return self.__A // self.__B

    def double(self):
        """преобразования дроби в тип float"""
        return self.__A / self.__B


def convert_a_string_to_a_fraction(line):
    A = line[:line.index('/')]
    B = line[line.index('/')+1:]
    return Fract(A,B)


A = Fract(5, 2)
B = Fract(6, 4)
a = Fraction(5, 2)
b = Fraction(6, 4)
print(A > B)
print(a > b)
print(3 / A)
D=convert_a_string_to_a_fraction('5/6')
print(D)