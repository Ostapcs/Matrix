import numpy as np
import ast
import sys


class Matrix:

    def __init__(self, size=None, rows=None, column=None, wayofcreation="create"):
        self.indexrow = 0
        self.indexcolumn = 0
        if size is None or rows is None or column is None:
            raise ValueError('Error : Invalid parameters')

        elif rows * column != size:
            raise ValueError("Error : Can not reshape. Invalid parameters")

        if wayofcreation == "create":
            self.matrix = np.arange(size).reshape(rows, column)

        elif wayofcreation == "manually":
            self.matrix = np.arange(float(size))
            print("Input your matrix : ")
            for i in range(size):
                try:
                    self.matrix[i] = ast.literal_eval(input())
                except:
                    print(sys.exc_info()[0], " : ", sys.exc_info()[1])
            self.matrix = self.matrix.reshape(rows, column)

        else:
            raise SyntaxError("Error : Invalid wayofcreation parameters. It mast be equal \"create\" or \"manualy\"")

    def __add__(self, other):
        if self.matrix.shape[0] == other.matrix.shape[0] and self.matrix.shape[1] == other.matrix.shape[1]:
            self.matrix = self.matrix + other.matrix
            return self

        else:
            raise ValueError("Matrix's shapes should be equal")

    def __sub__(self, other):
        if self.matrix.shape[0] == other.matrix.shape[0] and self.matrix.shape[1] == other.matrix.shape[1]:
            self.matrix = self.matrix - other.matrix
            return self

        else:
            raise ValueError("Matrix's shapes should be equal")

    def __next__(self):

        try:
            element = self.matrix[self.indexcolumn][self.indexrow]
        except:
            raise StopIteration()
        if self.indexrow < self.matrix.shape[1] - 1 and self.indexcolumn <= self.matrix.shape[0] - 1:
            self.indexrow += 1
        else:
            self.indexcolumn += 1
            self.indexrow = 0

        return element

    def __iter__(self):
        self.indexrow = 0
        self.indexcolumn = 0
        return self

    def __mul__(self, other):
        if self.matrix.shape[0] == other.matrix.shape[0] and self.matrix.shape[1] == other.matrix.shape[1]:
            self.matrix = self.matrix @ other.matrix
            return self

        elif self.matrix.shape[1] == other.matrix.shape[0]:
            self.matrix = self.matrix @ other.matrix
            return self

        else:
            raise ValueError("First matrix's quantity of columns should be equal to second matrix's quantity of rows")

    def genSpiral(self):
        for v in range(int(np.ceil(self.matrix.shape[1] / 2))):
            i, j = v, v

            while j < self.matrix.shape[1] - 1 - v:
                yield self.matrix[i][j]
                j += 1

            while i < self.matrix.shape[0] - 1 - v:
                yield self.matrix[i][j]
                i += 1

            while j > v:
                yield self.matrix[i][j]
                j -= 1

            while i > v:
                yield self.matrix[i][j]
                i -= 1

        if self.matrix.shape[0] == self.matrix.shape[1]:
            yield self.matrix[self.matrix.shape[1]//2][self.matrix.shape[1]//2]

        # v = 0
        # while v < int(np.ceil((self.matrix.shape[1] / 2))):
        #     i, j = v, v
        #     while j < self.matrix.shape[1] - 1 - v:
        #         yield self.matrix[i][j]
        #         j += 1
        #
        #     while i < self.matrix.shape[0] - 1 - v:
        #         yield self.matrix[i][j]
        #         i += 1
        #
        #     while j > v:
        #         yield self.matrix[i][j]
        #         j -= 1
        #
        #     while i > v:
        #         yield self.matrix[i][j]
        #         i -= 1
        #
        #     v += 1
        # for v in range(self.matrix.shape[0] // 2):
        #
        #     for i in range(self.matrix.shape[1] - m):
        #         print(self.matrix[v][i + v])
        #
        #     for i in range(v + 1, self.matrix.shape[0] - v):
        #         print(self.matrix[i][-v - 1])
        #
        #     for i in range(v + 1, self.matrix.shape[1] - v):
        #         print(self.matrix[-v - 1][-i - 1])
        #
        #     for i in range(v + 1, self.matrix.shape[0] - (v + 1)):
        #         print(self.matrix[-i - 1][v])
        #
        #     m += 1
        # # yield self.matrix[self.matrix.shape[0]//2][self.matrix.shape[0]//2]

    def tanspose(self):
        self.matrix = np.transpose(self.matrix)
        return self

    def invertableMatrix(self):
        if np.linalg.det(self.matrix) == 0:
            raise np.linalg.LinAlgError("Can't find invertible matrix because the determinant of matrix is equal to 0")
        self.matrix = np.linalg.inv(self.matrix)
        return self

    def solve(self, other=None):
        if other is None:
            other = np.zeros(self.matrix.shape[1])

        if self.matrix.shape[1] == other.shape[0]:
            result = np.linalg.solve(self.matrix, other)

            if not np.allclose(self.matrix @ result, other):
                raise ValueError("OOOOpss")

            return result

    def norma(self):
        frobenius_norm = np.linalg.norm(self.matrix)
        norma1 = np.linalg.norm(self.matrix, np.inf)
        norma_infinity = np.linalg.norm(self.matrix, 1)
        return [frobenius_norm, norma1, norma_infinity]

    def Eig(self):
        # if self.matrix.shape[0] == self.matrix.shape[1]:
        #     return np.linalg.eig(self.matrix)
        # else:
        return np.linalg.eigvals(self.matrix)
