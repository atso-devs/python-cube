print("Введите количество строк в матрице (n) => ")
n = int(input())

print("Введите количество столбцов в матрице (m) => ")
m = int(input())

print("Введите количество матриц (k) => ")
k = int(input())

count = (n+1)*(m+1)
print("Общее количество точек в одной матрице => ", count)

print("Введите координату x => ")
x = int(input())

print("Введите координату y => ")
y = int(input())

print("Введите координату z => ")
z = int(input())

if (x > n):
    print("x не может быть больше n")
elif (y > m):
    print("y не может быть больше m")
elif (z > k):
    print("z не может быть больше k")
else:
    print()

    dot = (x + y) + (y * m + 1) + (count * z)
    print("Порядковый номер точки: ", dot)
