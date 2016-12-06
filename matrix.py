import numpy as np
import random
import operator
import sys
import unittest

a = np.array([[0, 1, 2], [4, 5, 6]])
a = a.transpose()


class Matrix(object):
    def __init__(self, m, n, init=True):
        if init:
            self.rows = [[0] * n for x in range(m)]
        else:
            self.rows = []
        self.m = m
        self.n = n

    def __getitem__(self, idx):
        return self.rows[idx]

    def __setitem__(self, idx, item):
        self.rows[idx] = item

    def __str__(self):
        s = '\n'.join([' '.join([str(item) for item in row]) for row in self.rows])
        return s + '\n'



    def transpose(self):


        self.m, self.n = self.n, self.m
        self.rows = [list(item) for item in zip(*self.rows)]

    def getTranspose(self):

        m, n = self.n, self.m
        mat = Matrix(m, n)
        mat.rows = [list(item) for item in zip(*self.rows)]

        return mat



    @classmethod
    def makeRandom(cls, m, n, low=0, high=10):

        obj = Matrix(m, n, init=False)
        for x in range(m):
            obj.rows.append([random.randrange(low, high) for i in range(obj.n)])

        return obj

    @classmethod
    def makeZero(cls, m, n):


        rows = [[0] * n for x in range(m)]
        return cls.fromList(rows)

    @classmethod
    def _makeMatrix(cls, rows):

        m = len(rows)
        n = len(rows[0])
        # Validity check
        mat = Matrix(m, n, init=False)
        mat.rows = rows

        return mat

    @classmethod
    def fromList(cls, listoflists):


        rows = listoflists[:]
        return cls._makeMatrix(rows)


    def col(self):
        self.rows = [list(item[::-1]) for item in self.rows]




m = Matrix.makeRandom(5,10)
print('Matrix\n', m)
m.transpose()
print('Transpose\n',m)
m = zip(*m[::-1])
print('Turn')
for m1 in m:
    print(m1)

m1 = list([[12, 18, 6, 3],
     [ 4,  3, 1, 2],
     [15,  8, 9, 6]])

print('Matrix\n', m1)
m1.sort(key=lambda x: x[1])
print('Sort\n',m1)

m = Matrix.makeRandom(5,10)
print('Matrix\n', m)
m.col()
print('Col\n', m)

