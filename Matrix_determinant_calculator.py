print("Введите количество строк в матрице:")
m = int(input())
print("Введите количество столбцов в матрице:")
n = int(input())
matrix = list()
for i in range(m):
    matrix.insert(i, [])
    for j in range(n):
        print("Введите значение элемента в позиции", str(i + 1), str(j + 1) + ":")
        matrix[i].insert(j, int(input()))
print()
print("Начальный вид матрицы:")
for item in matrix:
    print(item)
print()
pos_i, pos_j = 0, 0
while pos_i < m and pos_j < n:
    if matrix[pos_i][pos_j] != 0:
        for i in range(pos_i + 1, m):
            c = matrix[i][pos_j] / matrix[pos_i][pos_j]
            for j in range(pos_j, n):
                matrix[i][j] -= matrix[pos_i][j] * c
        pos_i, pos_j = pos_i + 1, pos_j + 1
    else:
        f = False
        for i in range(pos_i + 1, m):
            if matrix[i][pos_j] != 0:
                f = True
                b = matrix[i].copy()
                matrix[i] = matrix[pos_i].copy()
                matrix[pos_i] = b.copy()
                break
        if f == False:
            pos_j = pos_j + 1
for i in range(m):
    for j in range(n):
        if matrix[i][j] == int(matrix[i][j]):
            matrix[i][j] = int(matrix[i][j])
print("Верхний ступенчатый вид матрицы:")
for item in matrix:
    print(item)
print()
det = 1
pos_i, pos_j = 0, 0
while pos_i < m and pos_j < n:
    det = det * matrix[pos_i][pos_j]
    pos_i, pos_j = pos_i + 1, pos_j + 1
if det == int(det):
    det = int(det)
print("Определитель матрицы равен", det)
