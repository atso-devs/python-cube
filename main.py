import numpy as np

print("Введите количество строк матрицы: ")
i = int(input())

print("Введите количество столбцов матрицы: ")
j = int(input())

print("Введите количество матриц: ")
k = int(input())

ii = i
jj = j
kk = k

MatrixList = np.arange(i*j*k).reshape(k, i, j)
print(MatrixList)

print("Общее количество элементов матриц: " + str(MatrixList.size))

def Up(kk, ii, jj):
    for k in range(kk):
        for j in range(jj):
            print(MatrixList[k][ii][j], end="\t")
        print(" - Элементы матрицы: " + str(k+1), end="\t")
        print("", end="\n")

def Left(kk, ii, jj):
    for k in range(kk):
        for i in range(ii):
            print(MatrixList[k][i][jj], end="\t")
        print(" - Элементы матрицы: " + str(k+1), end="\t")
        print("", end="\n")

def Right(kk, ii, jj):
    for k in range(kk):
        for i in range(ii):
            print(MatrixList[k][i][jj], end="\t")
        print(" - Элементы матрицы: " + str(k+1), end="\t")
        print("", end="\n")

def Down(kk, ii, jj):
    for k in range(kk):
        for j in range(jj):
            print(MatrixList[k][ii][j], end="\t")
        print(" - Элементы матрицы: " + str(k+1), end="\t")
        print("", end="\n")

def SearchDot():
    print("Введите номер строки: ")
    x = int(input())

    print("Введите номер столбца: ")
    y = int(input())

    print("Введите номер матрицы: ")
    z = int(input())
    print("Число по координатам - " + "x:" + str(x) + " y:" + str(y) + " z:" + str(z))
    print(MatrixList[z-1][x-1][y-1])


def switch(switchNum):
    if switchNum == 1:
        Up(kk, 0, jj)
    elif switchNum == 2:
        Left(kk, ii, 0)
    elif switchNum == 3:
        Right(kk, ii, jj-1)
    elif switchNum == 4:
        Down(kk, ii-1, jj)
    elif switchNum == 5:
        SearchDot()


print("Выберите функционал: ")
print("1 - Верхняя грань")
print("2 - Левая грань")
print("3 - Правая грань")
print("4 - Нижняя грань")
print("5 - Найти число по координатам")

switchNum = int(input())

switch(switchNum)
