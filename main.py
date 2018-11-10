import sys
from UI import UI
import numpy as np
from Matrix import Matrix


def main():
    UI()
    # a = Matrix(4, 2, 2)
    # a.matrix[0][0] = 2
    # a.matrix[0][1] = 1
    # a.matrix[1][0] = 1
    # a.matrix[1][1] = 2
    #
    # # print(np.linalg.eigvals(a.matrix))
    # # print(np.linalg.eigh(a.matrix))
    # print(np.array([2,1,1,2]).reshape(2,2))
    # b,v = np.linalg.eig(np.array([2,1,1,2]).reshape(2,2))
    # print(b,v)
    # print(np.linalg.eigh(np.array([2,1,1,2]).reshape(2,2)))
    #
    # # print(a.matrix)
    # # for i in a.genSpiral():
    # #     print(i)


if __name__ == '__main__':
    main()
