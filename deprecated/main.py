def main():
    print("Введите координату x => ")
    x = int(input())

    print("Введите координату y => ")
    y = int(input())

    print("Введите координату z => ")
    z = int(input())

    if x > n:
        print("x не может быть больше n")
    elif y > m:
        print("y не может быть больше m")
    elif z > k:
        print("z не может быть больше k")
    else:
        dot = (x + y) + (y * m + 1) + (count * z)
        print("Порядковый номер точки: ", dot)


def topSide():
    x = 0
    y = 3
    z = 0

    print("Точки верхней грани куба: ")
    for z in range(k):
        for x in range(m + 1):
            print((x + y) + (y * m + 1) + (count * z))


def leftSide():
    x = 0
    y = n
    z = 0

    print("Точки левой грани куба: ")
    for z in range(k):
        for y in range(n + 1):
            print((x + y) + (y * m + 1) + (count * z))


def rightSide():
    x = m
    y = 0
    z = 0

    print("Точки правой грани куба: ")
    for z in range(k):
        for y in range(n + 1):
            print((x + y) + (y * m + 1) + (count * z))


def bottomSide():
    x = 0
    y = 0
    z = 0

    print("Точки нижней грани куба: ")
    for z in range(k):
        for x in range(m + 1):
            print((x + y) + (y * m + 1) + (count * z))


def action(num):
    if num == 1:
        main()
    elif num == 2:
        topSide()
    elif num == 3:
        leftSide()
    elif num == 4:
        rightSide()
    elif num == 5:
        bottomSide()


print("Выберите функционал: ")
print("1 - main")
print("2 - topSide")
print("3 - leftSide")
print("4 - rightSide")
print("5 - bottomSide")

num = int(input())

if (num > 5) and (num < 1):
    print("Введенные вами данные недопустимы. ")
else:
    print("Введите количество строк в матрице (n) => ")
    n = int(input())

    print("Введите количество столбцов в матрице (m) => ")
    m = int(input())

    print("Введите количество матриц (k) => ")
    k = int(input())

    count = (n + 1) * (m + 1)

    action(num)
