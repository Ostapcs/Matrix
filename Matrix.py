import numpy as np
import ast
import sys


class Matrix:

    def __init__(self, size=None, rows=None, column=None, wayofcreation="create"):
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

    def __mul__(self, other):
        if self.matrix.shape[0] == other.matrix.shape[0] and self.matrix.shape[1] == other.matrix.shape[1]:
            self.matrix = self.matrix @ other.matrix
            return self

        elif self.matrix.shape[1] == other.matrix.shape[0]:
            # result = np.empty([self.matrix.shape[0], other.matrix.shape[1]])
            # for i in range(self.matrix.shape[0]):
            #     res = 0
            #     for j in range(other.matrix.shape[1]):
            #         for k in range(self.matrix.shape[1]):
            #             res += self.matrix[i][k] * other.matrix[k][j]
            #         result[i][j] = res
            # self.matrix = result
            self.matrix = self.matrix @ other.matrix
            return self

        else:
            raise ValueError("First matrix's quantity of columns should be equal to second matrix's quantity of rows")

    def genSpiral(self):
        m = 0
        for v in range(self.matrix.shape[0] // 2):

            for i in range(self.matrix.shape[0] - m):
                yield self.matrix[v][i + v]

            for i in range(v + 1, self.matrix.shape[0] - v):
                yield self.matrix[i][-v - 1]

            for i in range(v + 1, self.matrix.shape[0] - v):
                yield self.matrix[-v-1][-i - 1]

            for i in range(v + 1, self.matrix.shape[0] - (v + 1)):
                yield self.matrix[-i - 1][v]

            m += 2
        yield self.matrix[self.matrix.shape[0]//2][self.matrix.shape[0]//2]

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
