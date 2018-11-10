from Matrix import Matrix
import sys
from numpy import zeros
from ast import literal_eval


def Enterparameters():
    size = int(input("Enter size of matrix : "))
    rows = int(input("Enter rows : "))
    column = int(input("Enter column : "))
    return [size, rows, column]


def info():
    """Available operations:
    1. addition
    2. subtraction
    3. multiply
    4. transpose
    5. solve
    6. invert
    7. norms
    8. exit
    """


def CreateMatrix():
    inp = input("If you want input matrix manually enter manually, else enter create :  ")
    mat = []
    while True:
        if inp == "create":
            items = Enterparameters()
            try:
                mat = Matrix(items[0], items[1], items[2])
                break
            except:
                print(sys.exc_info()[1])
                exit(0)
        elif inp == "manually":
            items = Enterparameters()
            try:
                mat = Matrix(items[0], items[1], items[2], "manually")
                break
            except:
                print(sys.exc_info()[1])
                exit(0)
        else:
            inp = input("Enter manually or create : ")

    return mat


def UI():
    mtrx = CreateMatrix()

    command = input("Enter help to get additional information about operations ")

    while True:
        if command == "help":
            print(info.__doc__)
            break
        else:
            command = input("Enter help to get additional information about operations : ")

    while True:
        command = input("Enter operation or enter exit if you want to close program : ")

        if command == "addition":
            print("Create second matrix")
            othermtrx = CreateMatrix()
            try:
                mtrx = mtrx + othermtrx
                print(mtrx.matrix)
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)

        elif command == "subtraction":
            print("Create second matrix")
            othermtrx = CreateMatrix()
            try:
                mtrx = mtrx - othermtrx
                print(mtrx.matrix)
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)

        elif command == "multiply":
            print("Create second matrix")
            othermtrx = CreateMatrix()
            try:
                mtrx = mtrx * othermtrx
                print(mtrx.matrix)
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)

        elif command == "transpose":
            try:
                mtrx = mtrx.tanspose()
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)

        elif command == "solve":
            inpt = input("Create a vector. You can skip it, then program create vector that contains zeros : ")
            vec = None
            if inpt == "create":
                vec = zeros(mtrx.matrix.shape[1])
                for i in range(len(vec)):
                    vec[i] = literal_eval(input())
            try:
                print(mtrx.solve(vec))
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)

        elif command == "invert":
            try:
                mtrx = mtrx.invertableMatrix()
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)

        elif command == "norms":
            try:
                items = mtrx.norma()
                print("""||A||_F = {0}\n||A||_1 = {1}\n||A||_infinity = {2}""".format(items[0], items[1], items[2]))
            except:
                print(sys.exc_info()[0], " : ", sys.exc_info()[1])
                exit(0)
        elif command == "exit":
            exit(1)

        else:
            continue
