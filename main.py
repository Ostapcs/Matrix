import sys
from UI import UI
import numpy as np
from Matrix import Matrix

# фільтри
# вибірки
def main():
    # UI()
    a = Matrix(25,5,5)
    print(a.matrix)
    for i in a.genSpiral():
        print(i)
    #
    # sd = Matrix(6, 2, 3)
    # fg = Matrix(6,2,3)
    # sd = sd - fg
    # for i in sd:
    #     # if np.where(sd.matrix == i)[1] == sd.matrix.shape[1] - 1:
    #     #     print(i, end="\n")
    #     # else:
    #     print(list(sd).index(0))
    # print(np.where(sd.matrix == 0))
    # print(list(sd).index(0))

    # for i in sd:
    #     print(i)
    #
    # for i in sd:
    #     print(i)
    # count = 0
    # i = np.where(sd.matrix == 3)
    # print(np.where(sd.matrix == 3))
    # for i in sd:
    #     if np.where(sd.matrix == i)[1] == sd.matrix.shape[1] - 1:
    #         print(i,end="\n")
    #     else:
    #         print(i,end=" ")


if __name__ == '__main__':
    main()
