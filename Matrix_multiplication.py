# сделать матрицу
x, y = [int(i) for i in input().split()]
matrix = []
for i in range(x):
    row = []
    for j in range(y):
        row.append(1)
    matrix.append(row)

# тройной цикл по наполнению
xy = 0
for q in range(x * y):
    for i in range(x):
        for j in range(y):
            if i + j == q:
                xy += 1
                matrix[i][j] = str(xy).ljust(2)

# пустить на печать
for i in matrix:
    print(*i)