print("Введите количество строк в матрице (n) => ")
n = int(input())

print("Введите количество столбцов в матрице (m) => ")
m = int(input())

print("Введите количество матриц (k) => ")
k = int(input())

count = (n+1)*(m+1)
print("Общее количество точек в одной матрице => ", count)

x = 0
y = 3
z = 0

print("Точки верхней грани куба: ")
for z in range(k):
    for x in range(m+1):
        print((x + y) + (y * m + 1) + (count * z))
