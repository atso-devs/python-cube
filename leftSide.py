print("Введите количество строк в матрице (n) => ")
n = int(input())

print("Введите количество столбцов в матрице (m) => ")
m = int(input())

print("Введите количество матриц (k) => ")
k = int(input())

count = (n+1)*(m+1)
print("Общее количество точек в одной матрице => ", count)

x = 0
y = n
z = 0

print("Точки левой грани куба: ")
for z in range(k):
    for y in range(n+1):
        print((x + y) + (y * m + 1) + (count * z))
